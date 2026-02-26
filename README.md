# Dynasty League Manager

A scalable Flask starter app for managing a dynasty fantasy football league with Sleeper data.

## What this first version includes

- Application factory pattern (`create_app`) so the project can scale cleanly.
- Blueprint-based routing (`main` blueprint).
- Dedicated Sleeper API client service layer.
- League snapshot domain service to compose league, teams, lineups, and matchup data.
- Basic web UI to:
  - enter a Sleeper league ID
  - optionally choose a week
  - view league overview, teams, starters, and matchup scoring
- Initial unit test for the service layer.

## Tech stack

- Python 3.9+
- Flask
- urllib (Python standard library)
- Pytest

## Project structure

```text
Dynasty-League-Manager/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main/
│   │   └── routes.py
│   ├── services/
│   │   ├── league_service.py
│   │   └── sleeper_client.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── league.html
├── tests/
│   └── test_league_service.py
├── run.py
├── requirements.txt
└── README.md
```

## Getting started

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python run.py
   ```

4. Open in browser:

   ```text
   http://127.0.0.1:5000
   ```

## Sleeper API endpoints used

- `GET /v1/league/{league_id}`
- `GET /v1/league/{league_id}/users`
- `GET /v1/league/{league_id}/rosters`
- `GET /v1/state/nfl`
- `GET /v1/league/{league_id}/matchups/{week}`

## Next scalable steps

- Persist league snapshots and historical weeks in a database.
- Add async/background jobs for scheduled sync.
- Add authentication and user-specific saved leagues.
- Add player metadata resolution for starter IDs to player names.
- Split into API + frontend clients if you want mobile support later.
