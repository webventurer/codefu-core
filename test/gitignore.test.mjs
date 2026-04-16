import { strictEqual } from "node:assert";
import { describe, it } from "node:test";
import {
  buildSection,
  GITIGNORE_BEGIN,
  GITIGNORE_END,
  removeSection,
} from "../bin/gitignore.mjs";

describe("buildSection", () => {
  it("wraps entries in markers", () => {
    const section = buildSection([".claude/tools/", ".claude/stride/"]);

    strictEqual(
      section,
      `${GITIGNORE_BEGIN}\n.claude/tools/\n.claude/stride/\n${GITIGNORE_END}`,
    );
  });

  it("handles empty entries", () => {
    strictEqual(buildSection([]), `${GITIGNORE_BEGIN}\n${GITIGNORE_END}`);
  });
});

describe("removeSection", () => {
  it("strips section between markers", () => {
    const input = `node_modules\n${GITIGNORE_BEGIN}\n.claude/tools/\n${GITIGNORE_END}\n.env\n`;

    strictEqual(removeSection(input), "node_modules\n\n.env\n");
  });

  it("returns content unchanged when no markers present", () => {
    const input = "node_modules\n.env\n";

    strictEqual(removeSection(input), input);
  });

  it("returns content unchanged when end marker missing (malformed)", () => {
    const input = `node_modules\n${GITIGNORE_BEGIN}\n.claude/tools/\n.env\n`;

    strictEqual(removeSection(input), input);
  });

  it("returns empty when input is only the section", () => {
    const input = `${GITIGNORE_BEGIN}\n.claude/tools/\n${GITIGNORE_END}\n`;

    strictEqual(removeSection(input), "");
  });

  it("preserves leading content when section is at the end", () => {
    const input = `node_modules\n${GITIGNORE_BEGIN}\n.claude/tools/\n${GITIGNORE_END}\n`;

    strictEqual(removeSection(input), "node_modules\n");
  });

  it("preserves trailing content when section is at the start", () => {
    const input = `${GITIGNORE_BEGIN}\n.claude/tools/\n${GITIGNORE_END}\n.env\n`;

    strictEqual(removeSection(input), ".env\n");
  });

  it("normalises excess blank lines around the removed section", () => {
    const input = `node_modules\n\n\n${GITIGNORE_BEGIN}\n.claude/tools/\n${GITIGNORE_END}\n\n\n.env\n`;

    strictEqual(removeSection(input), "node_modules\n\n.env\n");
  });
});
