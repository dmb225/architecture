import pytest

from application.entities.user import User
from infrastructure.databases.user.in_memory import InMemoryUserDatabase


@pytest.fixture
def user_database() -> InMemoryUserDatabase:
    return InMemoryUserDatabase()


@pytest.fixture
def user() -> User:
    return User(name="John Doe", email="john@example.com", password="password123", confirmed=False)


@pytest.mark.asyncio
async def test_add_user(user_database: InMemoryUserDatabase, user: User) -> None:
    await user_database.add(user)
    users = await user_database.get_all()

    assert len(users) == 1
    assert user.id in users
    assert users[user.id] == user


@pytest.mark.asyncio
async def test_get_user_by_id(user_database: InMemoryUserDatabase, user: User) -> None:
    await user_database.add(user)

    assert user == await user_database.get(id=user.id)


@pytest.mark.asyncio
async def test_update_user(user_database: InMemoryUserDatabase, user: User) -> None:
    await user_database.add(user)
    user.name = "Jane Doe"

    assert await user_database.update(user) is True
    updated_user = await user_database.get(id=user.id)
    assert updated_user
    assert updated_user.name == "Jane Doe"


@pytest.mark.asyncio
async def test_delete_user(user_database: InMemoryUserDatabase, user: User) -> None:
    await user_database.add(user)
    await user_database.delete(user.id) is True

    assert user.id not in user_database.storage
