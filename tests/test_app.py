from app.auth import require_owner
from app.models import User


def test_admin_can_see_any_invoice():
    require_owner(User(id=1, email="a@x", is_admin=True), owner_id=2)  # no exception
