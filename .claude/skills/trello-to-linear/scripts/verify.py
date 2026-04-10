import json
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
def main(trello_dir: str, linear_file: str):
    trello_cards = load_trello_cards(Path(trello_dir))
    linear_issues = load_linear_issues(Path(linear_file))

    check_counts(trello_cards, linear_issues)
    check_titles(trello_cards, linear_issues)
    check_order(trello_cards, linear_issues)
    check_descriptions(trello_cards, linear_issues)


def load_trello_cards(trello_dir: Path) -> list[dict]:
    cards = []
    for f in sorted(trello_dir.glob("[0-9]*.json")):
        cards.extend(json.loads(f.read_text()))
    return cards


def load_linear_issues(path: Path) -> list[dict]:
    raw = json.loads(path.read_text())
    if isinstance(raw, list) and raw and "text" in raw[0]:
        return json.loads(raw[0]["text"]).get("issues", [])
    if isinstance(raw, dict):
        return raw.get("issues", [])
    return raw


def check_counts(trello: list, linear: list):
    click.echo(f"Trello cards: {len(trello)}")
    click.echo(f"Linear issues: {len(linear)}")
    if len(trello) == len(linear):
        click.echo("  PASS: counts match")
    else:
        click.echo(f"  FAIL: {abs(len(trello) - len(linear))} difference")


def check_titles(trello: list, linear: list):
    trello_titles = {c["name"] for c in trello}
    linear_titles = {i["title"] for i in linear}

    missing = trello_titles - linear_titles
    extra = linear_titles - trello_titles

    if not missing and not extra:
        click.echo("  PASS: all titles match")
        return

    if missing:
        click.echo(f"  FAIL: {len(missing)} missing from Linear:")
        for t in sorted(missing)[:10]:
            click.echo(f"    - {t[:70]}")

    if extra:
        click.echo(f"  WARN: {len(extra)} extra in Linear:")
        for t in sorted(extra)[:10]:
            click.echo(f"    + {t[:70]}")


def check_order(trello: list, linear: list):
    linear_by_title = {i["title"]: i for i in linear}
    linear_sorted = sorted(linear, key=sort_key)

    matches = 0
    mismatches = 0
    for i, card in enumerate(trello):
        if i >= len(linear_sorted):
            break
        if card["name"] == linear_sorted[i]["title"]:
            matches += 1
        else:
            mismatches += 1

    total = matches + mismatches
    click.echo(f"  Order: {matches}/{total} in correct position")
    if mismatches > 0:
        click.echo(f"  WARN: {mismatches} out of order")


def sort_key(issue: dict):
    return issue.get("createdAt", issue.get("sortOrder", ""))


def check_descriptions(trello: list, linear: list):
    linear_by_title = {i["title"]: i for i in linear}
    checked = 0
    passed = 0

    for card in trello:
        issue = linear_by_title.get(card["name"])
        if not issue:
            continue

        desc = issue.get("description", "") or ""
        trello_desc = card.get("description", "")

        if trello_desc and trello_desc in desc:
            passed += 1
        elif not trello_desc:
            passed += 1

        checked += 1

    click.echo(f"  Descriptions: {passed}/{checked} contain Trello content")
    if passed < checked:
        click.echo(f"  WARN: {checked - passed} descriptions missing content")


if __name__ == "__main__":
    main()
