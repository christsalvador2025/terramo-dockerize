import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from typing import Optional


class TerramoModuleBaseSchema(SQLModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        unique=True,
        nullable=False,
        description="Name of the module (e.g., 'ESG Check')",
    )
    description: Optional[str] = Field(
        default=None,
        description="Description of the module",
    )
    is_consultant_exclusive: bool = Field(
        default=False,
        description="True if module is exclusive to consultants by default",
    )

class TerramoModuleCreateSchema(TerramoModuleBaseSchema):
    pass

class TerramoModuleReadSchema(TerramoModuleBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class TerramoModuleUpdateSchema(TerramoModuleBaseSchema):
    name: str | None = None
   
