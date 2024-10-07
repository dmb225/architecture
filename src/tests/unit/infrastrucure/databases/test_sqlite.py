import pytest
from dataclasses import asdict
from sqlalchemy import create_engine

from application.entities.user import User
from infrastructure.databases.sqlite import SQLiteDatabase
from infrastructure.databases.models import Base

DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="function")
def sqlite_db() -> SQLiteDatabase:  # type: ignore
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(engine)
    db = SQLiteDatabase(engine, "user")
    yield db
    Base.metadata.drop_all(engine)


def test_add_and_get_user(sqlite_db: SQLiteDatabase) -> None:
    user = User(name="Alice", email="alice@example.com", password="securepass", confirmed=True)
    sqlite_db.add(asdict(user))
    fetched_user = sqlite_db.get(user.id)

    assert fetched_user is not None, "User should be added and fetched"
    assert fetched_user["name"] == user.name
    assert fetched_user["email"] == user.email
    assert fetched_user["password"] == user.password
    assert fetched_user["confirmed"] == user.confirmed


def test_update_user(sqlite_db: SQLiteDatabase) -> None:
    """Test updating a user."""
    user = User(name="Bob", email="bob@example.com", password="secret", confirmed=True)
    sqlite_db.add(asdict(user))

    updated_data = asdict(user)
    updated_data["name"] = "Updated Bob"
    updated_data["email"] = "updated_bob@example.com"
    sqlite_db.update(updated_data)
    fetched_user = sqlite_db.get(user.id)

    assert fetched_user is not None, "User should exist"
    assert fetched_user["name"] == "Updated Bob"
    assert fetched_user["email"] == "updated_bob@example.com"


def test_delete_user(sqlite_db: SQLiteDatabase) -> None:
    user = User(name="Charlie", email="charlie@example.com", password="topsecret", confirmed=False)
    sqlite_db.add(asdict(user))
    sqlite_db.delete(user.id)
    fetched_user = sqlite_db.get(user.id)

    assert fetched_user is None, "User should be deleted"


def test_list_all_users(sqlite_db: SQLiteDatabase) -> None:
    """Test listing all users."""
    user1 = User(name="User One", email="user1@example.com", password="pass1", confirmed=True)
    user2 = User(name="User Two", email="user2@example.com", password="pass2", confirmed=False)

    sqlite_db.add(asdict(user1))
    sqlite_db.add(asdict(user2))
    all_users = sqlite_db.list_all()

    assert len(all_users) == 2, "There should be two users in the database"
    assert all_users[0]["name"] == user1.name or all_users[1]["name"] == user1.name
    assert all_users[0]["email"] == user2.email or all_users[1]["email"] == user2.email
