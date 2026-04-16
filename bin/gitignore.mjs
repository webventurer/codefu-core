export const GITIGNORE_BEGIN = "# >>> stride (auto-managed, do not edit) >>>";
export const GITIGNORE_END = "# <<< stride <<<";

export function buildSection(entries) {
  return [GITIGNORE_BEGIN, ...entries, GITIGNORE_END].join("\n");
}

export function removeSection(content) {
  const beginIdx = content.indexOf(GITIGNORE_BEGIN);
  if (beginIdx === -1) return content;
  const endIdx = content.indexOf(GITIGNORE_END, beginIdx);
  if (endIdx === -1) return content;
  const endNewline = content.indexOf("\n", endIdx);
  const sectionEnd = endNewline === -1 ? content.length : endNewline + 1;
  const before = content.slice(0, beginIdx).replace(/\n+$/, "");
  const after = content.slice(sectionEnd).replace(/^\n+/, "");
  if (!before && !after) return "";
  if (!before) return after;
  if (!after) return `${before}\n`;
  return `${before}\n\n${after}`;
}
