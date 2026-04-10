import json
import os
import re
from pathlib import Path

import click
import requests

TRELLO_KEY = os.environ.get("TRELLO_API_KEY")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")
BASE = "https://api.trello.com/1"


@click.command()
@click.option("--board-id", required=True, help="Trello board ID")
@click.option(
    "--output", required=True, type=click.Path(), help="Output directory"
)
def main(board_id: str, output: str):
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)

    lists = fetch_lists(board_id)
    cards = fetch_all_cards(board_id)
    enrich_with_comments(cards)
    grouped = group_by_list(cards, lists)

    write_list_files(grouped, out)
    write_all_cards(cards, out)
    write_summary(grouped, out)
    click.echo(
        f"Exported {len(cards)} cards across {len(lists)} lists to {out}"
    )


def fetch_lists(board_id: str) -> dict[str, str]:
    url = f"{BASE}/boards/{board_id}/lists"
    params = auth_params() | {"filter": "all"}
    data = requests.get(url, params=params).json()
    return {lst["id"]: lst["name"] for lst in data}


def fetch_all_cards(board_id: str) -> list[dict]:
    url = f"{BASE}/boards/{board_id}/cards/all"
    params = auth_params() | {"fields": "name,desc,idList,shortUrl,closed"}
    data = requests.get(url, params=params).json()
    return [card_record(c) for c in data]


def card_record(raw: dict) -> dict:
    return {
        "trello_id": raw["id"],
        "name": raw["name"],
        "description": raw.get("desc", ""),
        "list_id": raw.get("idList", ""),
        "url": raw.get("shortUrl", ""),
        "closed": raw.get("closed", False),
    }


def enrich_with_comments(cards: list[dict]):
    for card in cards:
        card["comments"] = fetch_comments(card["trello_id"])


def fetch_comments(card_id: str) -> list[dict]:
    url = f"{BASE}/cards/{card_id}/actions"
    params = auth_params() | {"filter": "commentCard"}
    data = requests.get(url, params=params).json()
    return [comment_record(a) for a in data]


def comment_record(action: dict) -> dict:
    return {
        "author": action.get("memberCreator", {}).get("fullName", "Unknown"),
        "date": action.get("date", ""),
        "text": action.get("data", {}).get("text", ""),
    }


def group_by_list(
    cards: list[dict], lists: dict[str, str]
) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {name: [] for name in lists.values()}
    for card in cards:
        list_name = lists.get(card["list_id"], "Unknown")
        card["list"] = list_name
        grouped.setdefault(list_name, []).append(card)
    return grouped


def write_list_files(grouped: dict[str, list[dict]], out: Path):
    for i, (list_name, cards) in enumerate(sorted(grouped.items()), 1):
        slug = slugify(list_name)
        path = out / f"{i:02d}-{slug}.json"
        path.write_text(json.dumps(cards, indent=2))


def write_all_cards(cards: list[dict], out: Path):
    path = out / "all_cards.json"
    path.write_text(json.dumps(cards, indent=2))


def write_summary(grouped: dict[str, list[dict]], out: Path):
    all_cards = [c for cards in grouped.values() for c in cards]
    lines = summary_header(all_cards) + summary_table(grouped)
    (out / "SUMMARY.md").write_text("\n".join(lines) + "\n")


def count_with(cards: list[dict], field: str) -> int:
    return sum(1 for c in cards if c[field])


def summary_header(cards: list[dict]) -> list[str]:
    return [
        "# Trello export summary\n",
        f"**Total cards**: {len(cards)}",
        f"**With descriptions**: {count_with(cards, 'description')}",
        f"**With comments**: {count_with(cards, 'comments')}\n",
    ]


def summary_table(grouped: dict[str, list[dict]]) -> list[str]:
    lines = [
        "| List | Cards | With desc | With comments |",
        "|:-----|------:|----------:|--------------:|",
    ]
    for name in sorted(grouped):
        cards = grouped[name]
        lines.append(
            f"| {name} | {len(cards)} | {count_with(cards, 'description')} | {count_with(cards, 'comments')} |"
        )
    return lines


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def auth_params() -> dict[str, str]:
    return {"key": TRELLO_KEY, "token": TRELLO_TOKEN}


if __name__ == "__main__":
    main()
