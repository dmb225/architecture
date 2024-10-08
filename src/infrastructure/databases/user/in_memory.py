from typing import Any
from uuid import UUID

from application.entities.user import User
from application.interfaces.user_database import UserDatabase


class InMemoryUserDatabase(UserDatabase):
    storage: dict[UUID, User] = {}

    async def get(self, **filters: Any) -> User | None:
        if (f := filters.get("id")) and f in self.storage:
            return self.storage[f]
        return None

    async def add(self, user: User) -> None:
        self.storage[user.id] = user

    async def update(self, user: User) -> bool:
        if user.id in self.storage:
            self.storage[user.id] = user
            return True
        return False

    async def delete(self, id: UUID) -> bool:
        if id in self.storage:
            del self.storage[id]
            return True
        return False

    async def get_all(self) -> dict[UUID, User]:
        return self.storage
