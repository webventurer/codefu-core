import json
import re
from difflib import SequenceMatcher
from pathlib import Path

import click


@click.command()
@click.option(
    "--trello-dir",
    required=True,
    type=click.Path(exists=True),
    help="Trello export directory",
)
@click.option(
    "--linear-file",
    required=True,
    type=click.Path(exists=True),
    help="Linear issues JSON file",
)
@click.option("--threshold", default=0.85, help="Fuzzy match threshold (0-1)")
def main(trello_dir: str, linear_file: str, threshold: float):
    trello_cards = load_trello_cards(Path(trello_dir))
    linear_issues = load_linear_issues(Path(linear_file))
    report = build_match_report(trello_cards, linear_issues, threshold)

    out_path = Path(trello_dir) / "match-report.json"
    out_path.write_text(json.dumps(report, indent=2))
    print_summary(report)
    click.echo(f"\nMatch report written to {out_path}")


def load_trello_cards(trello_dir: Path) -> list[dict]:
    cards = []
    for f in sorted(trello_dir.glob("*.json")):
        if f.name in ("all_cards.json", "match-report.json"):
            continue
        cards.extend(json.loads(f.read_text()))
    return cards


def load_linear_issues(path: Path) -> list[dict]:
    raw = json.loads(path.read_text())
    if isinstance(raw, list) and raw and "text" in raw[0]:
        return json.loads(raw[0]["text"]).get("issues", [])
    if isinstance(raw, dict):
        return raw.get("issues", [])
    return raw


def build_match_report(
    trello_cards: list[dict],
    linear_issues: list[dict],
    threshold: float,
) -> list[dict]:
    linear_by_title = {normalise(i["title"]): i for i in linear_issues}
    return [
        find_match(card, linear_by_title, threshold) for card in trello_cards
    ]


def find_match(card: dict, linear_by_title: dict, threshold: float) -> dict:
    normalised_name = normalise(card["name"])
    entry = base_entry(card)

    if exact := linear_by_title.get(normalised_name):
        return entry | linear_fields(exact, "exact")

    if fuzzy := best_fuzzy_match(normalised_name, linear_by_title, threshold):
        return entry | linear_fields(fuzzy, "fuzzy")

    return entry | {"action": "create"}


def base_entry(card: dict) -> dict:
    return {
        "trello_name": card["name"],
        "trello_list": card.get("list", ""),
        "trello_description": card.get("description", ""),
        "trello_comments": card.get("comments", []),
        "trello_url": card.get("url", ""),
    }


def linear_fields(issue: dict, match_type: str) -> dict:
    has_desc = bool(issue.get("description"))
    action = "skip" if has_desc else "update"
    return {
        "linear_id": issue.get("id", ""),
        "linear_identifier": issue.get("identifier", ""),
        "linear_title": issue.get("title", ""),
        "linear_has_description": has_desc,
        "match_type": match_type,
        "action": action,
    }


def best_fuzzy_match(
    name: str,
    linear_by_title: dict,
    threshold: float,
) -> dict | None:
    best_score = 0.0
    best_issue = None

    for title, issue in linear_by_title.items():
        score = SequenceMatcher(None, name, title).ratio()
        if score > best_score:
            best_score, best_issue = score, issue

    return best_issue if best_score >= threshold else None


def normalise(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text)


def print_summary(report: list[dict]):
    updates = [r for r in report if r["action"] == "update"]
    creates = [r for r in report if r["action"] == "create"]
    skips = [r for r in report if r["action"] == "skip"]
    fuzzy = [r for r in report if r.get("match_type") == "fuzzy"]

    click.echo(f"Total cards: {len(report)}")
    click.echo(f"  Update (empty in Linear):  {len(updates)}")
    click.echo(f"  Create (no match):         {len(creates)}")
    click.echo(f"  Skip (already has desc):   {len(skips)}")
    click.echo(f"  Fuzzy matches (review):    {len(fuzzy)}")


if __name__ == "__main__":
    main()
