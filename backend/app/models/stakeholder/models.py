import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from sqlalchemy import func, text
from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, Relationship

from backend.app.models.stakeholder.schema import StakeholderBaseSchema


if TYPE_CHECKING:
    from backend.app.auth.models import User



class Stakeholder(StakeholderBaseSchema, table=True):
 
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

    # Relationships
    #user_id: uuid.UUID = Field(foreign_key="user.id", ondelete="CASCADE") # FK
    # user: "User" = Relationship(back_populates="country") # Relation
    stakeholder_created_by: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    # country_updated_by: Optional[int] = Field(default=None, foreign_key="user.id")
    stakeholder_updated_by: Optional[uuid.UUID] = Field(default=None, foreign_key="user.id")
    
    created_by_user: "User" = Relationship(
        back_populates="stakeholders_created",
        sa_relationship_kwargs={"foreign_keys": "Stakeholder.stakeholder_created_by"}
    )
    updated_by_user: Optional["User"] = Relationship(
        back_populates="stakeholders_updated",
        sa_relationship_kwargs={"foreign_keys": "Stakeholder.stakeholder_updated_by"}
    )

   