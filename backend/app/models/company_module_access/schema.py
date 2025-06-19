import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from sqlalchemy.dialects import postgresql as pg


class CompanyModuleAccessBaseSchema(SQLModel):
    name: str = Field(min_length=2, max_length=100)
    reporting_year: int = Field(
        nullable=False,
        description="The specific reporting year for access",
    )
    is_purchased: bool = Field(
        default=False,
        description="True if the client has purchased this module",
    )
    is_active: bool = Field(
        default=False,
        description="True if the module is activated for the client",
    )

class CompanyModuleAccessCreateSchema(CompanyModuleAccessBaseSchema):
    pass


class CompanyModuleAccessReadSchema(CompanyModuleAccessBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class CompanyModuleAccessUpdateSchema(CompanyModuleAccessBaseSchema):
    name: str | None = None
   
