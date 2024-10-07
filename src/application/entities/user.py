from dataclasses import dataclass, field
from typing import Any, Self
from uuid import UUID, uuid4


@dataclass
class User:
    name: str
    email: str
    password: str
    confirmed: bool
    id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "confirmed": self.confirmed,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id=UUID(data["id"]),
            name=data["name"],
            email=data["email"],
            password=data["password"],
            confirmed=data["confirmed"],
        )
