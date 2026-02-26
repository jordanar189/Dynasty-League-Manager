from __future__ import annotations

from flask import Blueprint, current_app, render_template, request

from app.services.league_service import LeagueService
from app.services.sleeper_client import SleeperAPIError, SleeperClient

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    return render_template("index.html")


@main_bp.get("/league")
def league_view():
    league_id = request.args.get("league_id", "").strip()
    week_param = request.args.get("week", "").strip()

    if not league_id:
        return render_template("index.html", error="Please provide a Sleeper league ID.")

    week = int(week_param) if week_param.isdigit() else None

    sleeper_client = SleeperClient(base_url=current_app.config["SLEEPER_BASE_URL"])
    service = LeagueService(sleeper_client)

    try:
        league_snapshot = service.get_league_snapshot(league_id=league_id, week=week)
    except SleeperAPIError as exc:
        return render_template("index.html", error=str(exc), league_id=league_id, week=week_param)

    return render_template(
        "league.html",
        league_snapshot=league_snapshot,
        league_id=league_id,
    )
