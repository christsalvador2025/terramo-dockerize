import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from backend.app.esg_check.enums import ESGCheckCategory
from typing import Optional
from decimal import Decimal
from typing_extensions import Annotated

class EsgCheckBaseSchema(SQLModel):
    name: str = Field(
        max_length=255,
        unique=True,
        nullable=False,
        description="Name of the stakeholder",
    )
    priority: int = Field(
        nullable=False,
        description="ESG Check priority",
    )
    status_quo: Annotated[Decimal, Field(decimal_places=2)]
    esg_check_key: Optional[str] = Field(default=None, max_length=10)
    category: ESGCheckCategory


class EsgCheckCreateSchema(EsgCheckBaseSchema):
    pass


class EsgCheckReadSchema(EsgCheckBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class EsgCheckUpdateSchema(EsgCheckBaseSchema):
    name: str | None = None
   
