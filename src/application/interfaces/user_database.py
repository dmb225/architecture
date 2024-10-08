from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from application.entities.user import User


class UserDatabase(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> User | None:
        pass

    @abstractmethod
    async def add(self, user: User) -> None:
        pass

    @abstractmethod
    async def update(self, user: User) -> bool:
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> bool:
        pass

    @abstractmethod
    async def get_all(self) -> dict[UUID, User]:
        pass
