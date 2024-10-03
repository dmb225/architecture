from uuid import UUID

from core.entities.user import User


def test_user_creation():
    user = User(
        name="Alice Smith", email="alice@example.com", password="securepassword", confirmed=False
    )

    assert user.name == "Alice Smith"
    assert user.email == "alice@example.com"
    assert user.password == "securepassword"
    assert user.confirmed is False
    assert isinstance(user.id, UUID)


def test_user_default_id():
    user1 = User(
        name="Alice Smith", email="alice@example.com", password="securepassword", confirmed=False
    )
    user2 = User(
        name="Bob Brown", email="bob@example.com", password="anothersecurepassword", confirmed=True
    )

    assert user1.id != user2.id


def test_user_email_format():
    user = User(
        name="Alice Smith", email="alice@example.com", password="securepassword", confirmed=False
    )

    assert "@" in user.email
    assert "." in user.email.split("@")[-1]


def test_user_confirmation():
    user = User(
        name="Alice Smith", email="alice@example.com", password="securepassword", confirmed=True
    )
    assert user.confirmed is True
