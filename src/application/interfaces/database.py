from abc import ABC, abstractmethod
from typing import Generic, Protocol, TypeVar, Optional
from uuid import UUID


class HasID(Protocol):
    id: UUID  # Enforce that any entity passed to the repository must have an `id` attribute


T = TypeVar("T", bound=HasID)


class Database(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, id: UUID) -> Optional[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[T]:
        pass
