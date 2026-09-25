import pytest
from werkzeug.exceptions import Forbidden

from app.auth import require_owner
from app.models import User


def test_user_cannot_read_someone_elses_invoice():
    with pytest.raises(Forbidden):
        require_owner(User(id=1, email="a@x"), owner_id=2)


def test_owner_can_read_their_own_invoice():
    require_owner(User(id=2, email="b@x"), owner_id=2)  # no exception
