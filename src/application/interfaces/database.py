from abc import ABC, abstractmethod
from typing import Any, Optional
from uuid import UUID


class Database(ABC):
    @abstractmethod
    def add(self, entity: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get(self, id: UUID) -> Optional[dict[str, Any]]:
        pass

    @abstractmethod
    def update(self, entity: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[dict[str, Any]]:
        pass
