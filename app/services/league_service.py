from __future__ import annotations

from collections import defaultdict

from .sleeper_client import SleeperClient


class LeagueService:
    def __init__(self, sleeper_client: SleeperClient) -> None:
        self.sleeper_client = sleeper_client

    def get_league_snapshot(self, league_id: str, week: int | None = None) -> dict:
        league = self.sleeper_client.get_league(league_id)
        users = self.sleeper_client.get_league_users(league_id)
        rosters = self.sleeper_client.get_league_rosters(league_id)

        if week is None:
            nfl_state = self.sleeper_client.get_nfl_state()
            week = int(nfl_state.get("week", 1))

        matchup_rows = self.sleeper_client.get_matchups(league_id, week)

        users_by_id = {user["user_id"]: user for user in users}
        team_views = []

        for roster in rosters:
            owner_id = roster.get("owner_id")
            owner = users_by_id.get(owner_id, {})
            team_name = owner.get("metadata", {}).get("team_name") or owner.get("display_name", "Unknown")
            team_views.append(
                {
                    "roster_id": roster.get("roster_id"),
                    "team_name": team_name,
                    "owner": owner.get("display_name", "Unknown"),
                    "wins": roster.get("settings", {}).get("wins", 0),
                    "losses": roster.get("settings", {}).get("losses", 0),
                    "ties": roster.get("settings", {}).get("ties", 0),
                    "starters": roster.get("starters", []),
                }
            )

        matchups = defaultdict(list)
        for row in matchup_rows:
            matchups[row.get("matchup_id")].append(
                {
                    "roster_id": row.get("roster_id"),
                    "points": row.get("points", 0),
                    "starters": row.get("starters", []),
                }
            )

        return {
            "league": {
                "name": league.get("name", "Unknown League"),
                "season": league.get("season"),
                "total_rosters": league.get("total_rosters"),
            },
            "week": week,
            "teams": sorted(team_views, key=lambda team: team["roster_id"]),
            "matchups": dict(matchups),
        }
