from typing import Any, Generic, Type, TypeVar, Optional, List
from app.database.db import Base
from sqlalchemy.orm import Session
from app.database.db import get_database
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import joinedload


ModelType = TypeVar('ModelType', bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, model_id: Any, db: Session = next(get_database())) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == model_id).first()

    def get_relationships(self, model_id: Any, db: Session = next(get_database())) -> Optional[ModelType]:
        relations = inspect(self.model).relationships.items()

        query = db.query(self.model)
        for relation in relations:
            query = query.options(joinedload(relation[0]))
        query = query.filter(self.model.id == model_id).first()

        return query

    def get_multiple(self, db: Session = next(get_database())) -> Optional[List[ModelType]]:
        return db.query(self.model).all()
