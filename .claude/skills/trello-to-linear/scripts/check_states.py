"""Check that target Linear workspace has all mapped state names."""

import json
from pathlib import Path

import click
from linear_api import graphql, require_env, resolve_by_name


@click.command()
@click.option("--target-api-key-env", required=True)
@click.option("--target-team", required=True)
@click.option(
    "--state-map",
    required=True,
    type=click.Path(exists=True),
    help="JSON file mapping Trello list names to Linear state names",
)
def main(target_api_key_env: str, target_team: str, state_map: str):
    api_key = require_env(target_api_key_env)
    mapped_states = set(json.loads(Path(state_map).read_text()).values())
    target_states = fetch_target_states(api_key, target_team)
    target_names = {s["name"] for s in target_states}
    missing = mapped_states - target_names

    report(mapped_states, target_states, missing)

    if missing:
        raise SystemExit(1)


STATES_QUERY = """{{ workflowStates(filter: {{ team: {{ id: {{ eq: "{team_id}" }} }} }}) {{
    nodes {{ name type }}
}} }}"""


def fetch_target_states(api_key: str, team: str) -> list:
    team_id = resolve_by_name(api_key, "teams", team)
    return graphql(api_key, STATES_QUERY.format(team_id=team_id))["data"]["workflowStates"]["nodes"]


def report(mapped: set, target: list, missing: set):
    click.echo("Mapped states:")
    for name in sorted(mapped):
        marker = "✗" if name in missing else "✓"
        click.echo(f"  {marker} {name}")

    if not missing:
        click.echo("\nPASS: all mapped states exist in target")
        return

    click.echo(f"\nFAIL: {len(missing)} mapped state(s) missing from target:")
    for name in sorted(missing):
        click.echo(f"  - {name}")
    click.echo("\nTarget has:")
    for s in sorted(target, key=lambda x: x["name"]):
        click.echo(f"  {s['name']} ({s['type']})")


if __name__ == "__main__":
    main()
