from __future__ import annotations

from dataclasses import dataclass
import json
from urllib import error, request


class SleeperAPIError(Exception):
    """Raised when Sleeper API request fails."""


@dataclass
class SleeperClient:
    base_url: str
    timeout_seconds: int = 10

    def _get(self, path: str):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        try:
            with request.urlopen(url, timeout=self.timeout_seconds) as response:
                payload = response.read().decode("utf-8")
        except error.HTTPError as exc:
            message = exc.read().decode("utf-8", errors="replace")
            raise SleeperAPIError(f"Sleeper API error {exc.code}: {message}") from exc
        except error.URLError as exc:
            raise SleeperAPIError(f"Unable to reach Sleeper API: {exc.reason}") from exc

        return json.loads(payload)

    def get_league(self, league_id: str):
        return self._get(f"league/{league_id}")

    def get_league_users(self, league_id: str):
        return self._get(f"league/{league_id}/users")

    def get_league_rosters(self, league_id: str):
        return self._get(f"league/{league_id}/rosters")

    def get_matchups(self, league_id: str, week: int):
        return self._get(f"league/{league_id}/matchups/{week}")

    def get_nfl_state(self):
        return self._get("state/nfl")
