import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from backend.app.esg_check.enums import ESGCheckCategory
from typing import Optional
from decimal import Decimal
from typing_extensions import Annotated

class EsgCheckDescriptionBaseSchema(SQLModel):
    description_name: str = Field(
        max_length=255,
        unique=True,
        nullable=False,
    )
    country_iso: Optional[str] = Field(default=None, max_length=2)


class EsgCheckDescriptionCreateSchema(EsgCheckDescriptionBaseSchema):
    pass


class EsgCheckDescriptionReadSchema(EsgCheckDescriptionBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class EsgCheckDescriptionUpdateSchema(EsgCheckDescriptionBaseSchema):
    name: str | None = None
   
