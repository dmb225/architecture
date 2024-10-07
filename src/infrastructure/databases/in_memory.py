from typing import Any, Optional
from uuid import UUID

from application.interfaces.database import Database


class InMemoryDatabase(Database):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.storage: dict[str, Any] = {}

    def add(self, entity_data: dict[str, Any]) -> None:
        self.storage[entity_data["id"]] = entity_data

    def get(self, id: UUID) -> Optional[dict[str, Any]]:
        return self.storage.get(str(id))

    def update(self, entity_data: dict[str, Any]) -> None:
        if str(entity_data["id"]) in self.storage:
            self.storage[str(entity_data["id"])] = entity_data

    def delete(self, id: UUID) -> None:
        if str(id) in self.storage:
            del self.storage[str(id)]

    def list_all(self) -> list[dict[str, Any]]:
        return list(self.storage.values())
