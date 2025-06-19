import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import func, text
from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, Relationship

from backend.app.models.esg_check.schema import StakeholderBaseSchema

if TYPE_CHECKING:
    from backend.app.auth.models import User
    from backend.app.models.esg_check.models import EsgCheck
    from backend.app.models.esg_questionaire_answer.models import EsgCheckQuestionaireAnswer
 


class EsgCheckQuestionaire(StakeholderBaseSchema, table=True):
    id: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
        ),
        default_factory=uuid.uuid4,
    )
    
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            onupdate=func.current_timestamp(),
        ),
    )
    esg_check_id: uuid.UUID = Field(default=None, foreign_key="esgcheck.id")
    esg_check: "EsgCheck" = Relationship(back_populates="esg_check")
    esgcheck_created_by: uuid.UUID = Field(foreign_key="user.id", nullable=False)
 
    esgcheck_updated_by: Optional[uuid.UUID] = Field(default=None, foreign_key="user.id")
    
    # esg questionaire answers
    esg_questionaire_answer: List["EsgCheckQuestionaireAnswer"] = Relationship(back_populates="esg_questionaire_answer")

    created_by_user: "User" = Relationship(
        back_populates="countries_created",
        sa_relationship_kwargs={"foreign_keys": "Country.country_created_by"}
    )
    updated_by_user: Optional["User"] = Relationship(
        back_populates="countries_updated",
        sa_relationship_kwargs={"foreign_keys": "Country.country_updated_by"}
    )
    # Relationships
  
    