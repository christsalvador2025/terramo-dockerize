import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from sqlalchemy import func, text
from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, Relationship

from backend.app.models.esg_check.schema import StakeholderBaseSchema

if TYPE_CHECKING:
    from backend.app.auth.models import User
    from backend.app.models.esg_check_questionaire.models import EsgCheckQuestionaire
    from backend.app.models.esg_check.models import EsgCheck
 


class EsgCheckQuestionaireAnswer(StakeholderBaseSchema, table=True):
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

    # FK ESGCHECKQUESTIONAIRE
    esg_check_questionaire_id: uuid.UUID = Field(default=None, foreign_key="esg_check_questionaire.id")
    esg_check_questionaire: "EsgCheckQuestionaire" = Relationship(back_populates="esg_check_questionaire")

    # FK ESGCHECK
    esg_check_id: uuid.UUID = Field(default=None, foreign_key="esg_check.id")
    esg_check: "EsgCheck" = Relationship(back_populates="esg_check")

    # Relationships
  
    