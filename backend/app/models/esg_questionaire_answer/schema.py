import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from backend.app.esg_check.enums import ESGCheckCategory
from typing import Optional
from decimal import Decimal
from typing_extensions import Annotated

class EsgCheckQuestionaireBaseSchema(SQLModel):
    
    country_iso: Optional[str] = Field(default=None, max_length=2)


class EsgCheckQuestionaireCreateSchema(EsgCheckQuestionaireBaseSchema):
    pass


class EsgCheckQuestionaireReadSchema(EsgCheckQuestionaireBaseSchema):
    id: uuid.UUID
    user_id: uuid.UUID


class EsgCheckQuestionaireUpdateSchema(EsgCheckQuestionaireBaseSchema):
    name: str | None = None
   
