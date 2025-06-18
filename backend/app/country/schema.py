import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Column
from typing import Optional


class CountryBaseSchema(SQLModel):
    country_name: Optional[str] = Field(
        max_length=255,
        unique=True,
        nullable=False,
        description="Name of the client company",
    )
    country_iso_code: Optional[str] = Field(default=None, max_length=3)

class CountryCreateSchema(CountryBaseSchema):
    pass


class CountryReadSchema(CountryBaseSchema):
    id: uuid.UUID


class CountryUpdateSchema(CountryBaseSchema):
    name: str | None = None
   
