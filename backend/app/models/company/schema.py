import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Column



class CompanyBaseSchema(SQLModel):
    name: str = Field(
        max_length=255,
        unique=True,
        nullable=False,
        description="Name of the client company",
    )

class CompanyCreateSchema(CompanyBaseSchema):
    pass


class CompanyReadSchema(CompanyBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class CompanyUpdateSchema(CompanyBaseSchema):
    name: str | None = None
   
