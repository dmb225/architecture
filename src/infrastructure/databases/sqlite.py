from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from typing import Any, Optional, Type
from uuid import UUID

from application.interfaces.database import Database
from infrastructure.databases.models import Base, MODEL_MAP


class SQLiteDatabase(Database):
    def __init__(self, engine: Engine, model_name: str) -> None:
        self.engine = engine
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.model = self.get_model(model_name)

    def get_model(self, model_name: str) -> Type[Base]:
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise ValueError(f"Model '{model_name}' not found")
        return model

    def add(self, entity: dict[str, Any]) -> None:
        with self.Session() as session:
            session.add(self.model(**entity))
            session.commit()

    def get(self, id: UUID) -> Optional[dict[str, Any]]:
        with self.Session() as session:
            result = session.query(self.model).filter_by(id=id).first()
            return result.__dict__ if result else None

    def update(self, entity: dict[str, Any]) -> None:
        with self.Session() as session:
            obj = session.query(self.model).filter_by(id=entity["id"]).first()
            if obj:
                for key, value in entity.items():
                    setattr(obj, key, value)
                session.commit()

    def delete(self, id: UUID) -> None:
        with self.Session() as session:
            obj = session.query(self.model).filter_by(id=id).first()
            if obj:
                session.delete(obj)
                session.commit()

    def list_all(self) -> list[dict[str, Any]]:
        with self.Session() as session:
            return [obj.__dict__ for obj in session.query(self.model).all()]
