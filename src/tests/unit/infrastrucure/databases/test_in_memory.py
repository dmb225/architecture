import pytest

from application.entities.user import User
from infrastructure.databases.in_memory import InMemoryDatabase


@pytest.fixture
def in_memory_db() -> InMemoryDatabase[User]:
    return InMemoryDatabase[User]()


def test_in_memory_database_operations(in_memory_db: InMemoryDatabase[User]) -> None:
    # Test data
    user1 = User(name="John Doe", email="john@example.com", password="password123", confirmed=True)
    user2 = User(
        name="Jane Smith", email="jane@example.com", password="password456", confirmed=False
    )

    # 1. Add user1
    in_memory_db.add(user1)
    fetched_user1 = in_memory_db.get(user1.id)
    assert fetched_user1 is not None
    assert fetched_user1.name == user1.name
    assert fetched_user1.email == user1.email

    # 2. Update user1's name
    user1.name = "John Doe Updated"
    in_memory_db.update(user1)
    updated_user1 = in_memory_db.get(user1.id)
    assert updated_user1
    assert updated_user1.name == "John Doe Updated"

    # 3. Add user2
    in_memory_db.add(user2)
    fetched_user2 = in_memory_db.get(user2.id)
    assert fetched_user2 is not None
    assert fetched_user2.name == user2.name

    # 4. List all users
    all_users = in_memory_db.list_all()
    assert len(all_users) == 2
    assert user1 in all_users
    assert user2 in all_users

    # 5. Delete user1
    in_memory_db.delete(user1.id)
    deleted_user1 = in_memory_db.get(user1.id)
    assert deleted_user1 is None

    # 6. Check remaining users
    remaining_users = in_memory_db.list_all()
    assert len(remaining_users) == 1
    assert user2 in remaining_users
    assert user1 not in remaining_users

    # 7. Delete user2
    in_memory_db.delete(user2.id)
    deleted_user2 = in_memory_db.get(user2.id)
    assert deleted_user2 is None

    # 8. Final check for empty database
    assert in_memory_db.list_all() == []
