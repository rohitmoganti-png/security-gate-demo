from flask import abort, g

from app.models import User


def current_user() -> User:
    """The logged-in user for this request (set by the auth middleware)."""
    user = getattr(g, "user", None)
    if user is None:
        abort(401)
    return user


def require_owner(user: User, owner_id: int) -> None:
    """Reject the request unless the user owns the resource (admins may see everything)."""
    if user.id != owner_id and not user.is_admin:
        abort(403)
