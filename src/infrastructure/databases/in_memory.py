from typing import Optional
from uuid import UUID

from application.interfaces.database import T, Database


class InMemoryDatabase(Database[T]):
    def __init__(self) -> None:
        self._data: dict[UUID, T] = {}

    def add(self, entity: T) -> None:
        self._data[entity.id] = entity

    def get(self, id: UUID) -> Optional[T]:
        return self._data.get(id)

    def update(self, entity: T) -> None:
        if entity.id in self._data:
            self._data[entity.id] = entity

    def delete(self, id: UUID) -> None:
        if id in self._data:
            del self._data[id]

    def list_all(self) -> list[T]:
        return list(self._data.values())
