import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from backend.app.esg_check.enums import ESGCheckCategory


class EsgCheckBaseSchema(SQLModel):
    name: str = Field(
        max_length=255,
        unique=True,
        nullable=False,
        description="Name of the stakeholder",
    )
    category: ESGCheckCategory

class EsgCheckCreateSchema(EsgCheckBaseSchema):
    pass


class EsgCheckReadSchema(EsgCheckBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class EsgCheckUpdateSchema(EsgCheckBaseSchema):
    name: str | None = None
   
