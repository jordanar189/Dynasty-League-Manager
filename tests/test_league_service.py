from app.services.league_service import LeagueService


class FakeSleeperClient:
    def get_league(self, league_id: str):
        return {"name": "Test League", "season": "2024", "total_rosters": 2}

    def get_league_users(self, league_id: str):
        return [
            {"user_id": "1", "display_name": "Alice", "metadata": {"team_name": "A-Team"}},
            {"user_id": "2", "display_name": "Bob", "metadata": {}},
        ]

    def get_league_rosters(self, league_id: str):
        return [
            {
                "roster_id": 1,
                "owner_id": "1",
                "settings": {"wins": 3, "losses": 1, "ties": 0},
                "starters": ["QB1", "RB1"],
            },
            {
                "roster_id": 2,
                "owner_id": "2",
                "settings": {"wins": 2, "losses": 2, "ties": 0},
                "starters": ["QB2", "RB2"],
            },
        ]

    def get_matchups(self, league_id: str, week: int):
        return [
            {"matchup_id": 1, "roster_id": 1, "points": 100.5, "starters": ["QB1", "RB1"]},
            {"matchup_id": 1, "roster_id": 2, "points": 95.0, "starters": ["QB2", "RB2"]},
        ]

    def get_nfl_state(self):
        return {"week": 7}


def test_get_league_snapshot_builds_expected_shape():
    service = LeagueService(FakeSleeperClient())

    snapshot = service.get_league_snapshot("test-league")

    assert snapshot["league"]["name"] == "Test League"
    assert snapshot["week"] == 7
    assert len(snapshot["teams"]) == 2
    assert snapshot["teams"][0]["team_name"] == "A-Team"
    assert snapshot["teams"][1]["team_name"] == "Bob"
    assert len(snapshot["matchups"][1]) == 2
