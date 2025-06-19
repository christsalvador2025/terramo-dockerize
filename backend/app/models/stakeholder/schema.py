import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Column
from typing import Optional


class StakeholderBaseSchema(SQLModel):
    name: Optional[str] = Field(
        max_length=255,
        unique=True,
        nullable=False,
    )
    country_iso_code: Optional[str] = Field(default=None, max_length=3)

class StakeholderCreateSchema(StakeholderBaseSchema):
    pass


class StakeholderReadSchema(StakeholderBaseSchema):
    id: uuid.UUID


class StakeholderUpdateSchema(StakeholderBaseSchema):
    name: str | None = None
   
