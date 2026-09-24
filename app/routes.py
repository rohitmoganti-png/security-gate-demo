import requests
from flask import Blueprint, jsonify

from app.auth import current_user

bp = Blueprint("api", __name__)


@bp.get("/me")
def me():
    user = current_user()
    return jsonify(id=user.id, email=user.email)


@bp.get("/health")
def health():
    status_page_ok = False
    try:
        status_page_ok = requests.get("https://status.example.com", timeout=5).ok
    except Exception:
        pass  # pre-existing smell on main (warn-only): errors silently swallowed
    return jsonify(ok=True, status_page=status_page_ok)
