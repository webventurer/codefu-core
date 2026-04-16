import { strictEqual } from "node:assert";
import { execSync } from "node:child_process";
import {
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { dirname, join, relative } from "node:path";
import { after, describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const strideRoot = join(__dirname, "..");
const fixtureRoot = join("/tmp", `stride-footprint-${process.pid}`);

const SENTINELS = {
  "tools/format-mdx.sh": "consumer tool — must not change",
  "tools/remark/parse.mjs": "consumer remark plugin",
  "src/app.mjs": "consumer app code",
  "docs/README.md": "consumer docs",
  "package.json": '{"name":"consumer"}',
  ".env.example": "consumer env template",
  ".gitignore": "node_modules\n",
};

function seedFixture() {
  rmSync(fixtureRoot, { recursive: true, force: true });
  for (const [path, content] of Object.entries(SENTINELS)) {
    const full = join(fixtureRoot, path);
    mkdirSync(dirname(full), { recursive: true });
    writeFileSync(full, content);
  }
}

function runInstall({ gitignore = "n" } = {}) {
  // Prompts in order: gitignore, MCP (none), settings merge (n).
  const input = `${gitignore}\nnone\nn\n`;
  execSync(`node ${join(strideRoot, "bin/install.mjs")}`, {
    cwd: fixtureRoot,
    input,
    stdio: ["pipe", "pipe", "pipe"],
  });
}

function walk(dir, base = dir) {
  const paths = [];
  for (const entry of readdirSync(dir)) {
    if (entry === ".claude") continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) paths.push(...walk(full, base));
    else paths.push(relative(base, full));
  }
  return paths;
}

describe("install footprint", () => {
  after(() => rmSync(fixtureRoot, { recursive: true, force: true }));

  it("does not modify or delete files outside .claude/", () => {
    seedFixture();
    runInstall();

    for (const [path, expected] of Object.entries(SENTINELS)) {
      const actual = readFileSync(join(fixtureRoot, path), "utf8");
      strictEqual(actual, expected, `sentinel changed: ${path}`);
    }
  });

  it("does not create any new files outside .claude/", () => {
    seedFixture();
    runInstall();

    const after = new Set(walk(fixtureRoot));
    const expected = new Set(Object.keys(SENTINELS));
    for (const path of after) {
      strictEqual(expected.has(path), true, `unexpected file: ${path}`);
    }
    strictEqual(
      after.size,
      expected.size,
      "file count changed outside .claude/",
    );
  });

  it("creates the expected .claude/ subdirs", () => {
    seedFixture();
    runInstall();

    const claudeDir = join(fixtureRoot, ".claude");
    strictEqual(existsSync(join(claudeDir, "skills/commit")), true);
    strictEqual(existsSync(join(claudeDir, "commands/linear")), true);
    strictEqual(existsSync(join(claudeDir, "hooks")), true);
    strictEqual(existsSync(join(claudeDir, "tools/openrouter-chat.py")), true);
  });

  it("writes the stride section to .gitignore when accepted", () => {
    seedFixture();
    runInstall({ gitignore: "y" });

    const gitignore = readFileSync(join(fixtureRoot, ".gitignore"), "utf8");
    strictEqual(
      gitignore.includes("# >>> stride (auto-managed, do not edit) >>>"),
      true,
    );
    strictEqual(gitignore.includes("# <<< stride <<<"), true);
    strictEqual(gitignore.includes(".claude/tools/"), true);
    strictEqual(gitignore.includes(".claude/stride/"), true);
    strictEqual(
      gitignore.includes(
        ".claude/hooks/userpromptsubmit/inject_design_principles.sh",
      ),
      true,
    );
  });

  it("preserves existing .gitignore entries when adding the stride section", () => {
    seedFixture();
    runInstall({ gitignore: "y" });

    const gitignore = readFileSync(join(fixtureRoot, ".gitignore"), "utf8");
    strictEqual(gitignore.includes("node_modules"), true);
  });

  it("replaces an existing stride section rather than duplicating", () => {
    seedFixture();
    const existing = `node_modules\n\n# >>> stride (auto-managed, do not edit) >>>\n.claude/old-entry/\n# <<< stride <<<\n`;
    writeFileSync(join(fixtureRoot, ".gitignore"), existing);

    runInstall({ gitignore: "y" });

    const gitignore = readFileSync(join(fixtureRoot, ".gitignore"), "utf8");
    const matches = gitignore.match(/# >>> stride/g);
    strictEqual(matches?.length, 1, "stride section should not duplicate");
    strictEqual(gitignore.includes(".claude/old-entry/"), false);
    strictEqual(gitignore.includes(".claude/tools/"), true);
    strictEqual(gitignore.includes("node_modules"), true);
  });
});
