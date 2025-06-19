import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional, List

from pydantic import computed_field
from sqlalchemy import func, text
from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, Relationship

from backend.app.auth.schema import BaseUserSchema, RoleChoicesSchema

if TYPE_CHECKING:
    
    from backend.app.models.company.models import Company
    from backend.app.models.country.models import Country
    from backend.app.models.esg_check.models import EsgCheck
    from backend.app.models.esg_check_description.models import EsgCheckDescription
    from backend.app.models.user_profile.models import Profile
    from backend.app.models.stakeholder.models import Stakeholder

class User(BaseUserSchema, table=True):
    
    id: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
        ),
        default_factory=uuid.uuid4,
    )
    hashed_password: str
    failed_login_attempts: int = Field(default=0, sa_type=pg.SMALLINT)
    last_failed_login: datetime | None = Field(
        default=None, sa_column=Column(pg.TIMESTAMP(timezone=True))
    )
    otp: str = Field(max_length=6, default="")
    otp_expiry_time: datetime | None = Field(
        default=None, sa_column=Column(pg.TIMESTAMP(timezone=True))
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

    profile: "Profile" = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "lazy": "selectin",
        },
    )

    # --------- Country Relations -----------
    countries_created: List["Country"] = Relationship(
        back_populates="created_by_user",
        sa_relationship_kwargs={"foreign_keys": "Country.country_created_by"}
    )
    countries_updated: List["Country"] = Relationship(
        back_populates="updated_by_user",
        sa_relationship_kwargs={"foreign_keys": "Country.country_updated_by"}
    )

    # --------- ESG Check Relations -----------
    esgchecks_created: List["EsgCheck"] = Relationship(
        back_populates="created_by_user",
        sa_relationship_kwargs={"foreign_keys": "EsgCheck.esgcheck_created_by"}
    )
    esgchecks_updated: List["EsgCheck"] = Relationship(
        back_populates="updated_by_user",
        sa_relationship_kwargs={"foreign_keys": "EsgCheck.esgcheck_updated_by"}
    )

    # --------- ESG Check Description Relations -----------
    esgcheckdescriptions_created: List["EsgCheckDescription"] = Relationship(
        back_populates="created_by_user",
        sa_relationship_kwargs={"foreign_keys": "EsgCheckDescription.esgcheckdescription_created_by"}
    )
    esgcheckdescriptions_updated: List["EsgCheckDescription"] = Relationship(
        back_populates="updated_by_user",
        sa_relationship_kwargs={"foreign_keys": "EsgCheckDescription.esgcheckdescription_updated_by"}
    )
    
    # --------- Stakeholders Relations -----------
    stakeholders_created: List["Stakeholder"] = Relationship(
        back_populates="created_by_user",
        sa_relationship_kwargs={"foreign_keys": "Stakeholder.stakeholder_created_by"}
    )
    stakeholders_updated: List["Stakeholder"] = Relationship(
        back_populates="updated_by_user",
        sa_relationship_kwargs={"foreign_keys": "Stakeholder.stakeholder_updated_by"}
    )
    # Relationships
    # company: Optional["Company"] = Relationship(back_populates="users")

    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id", index=True)
    # client_id: Optional = Field(
    #     default=None, foreign_key="company.client_id", index=True
    # )

    company: "Company" = Relationship(back_populates="users")
    @computed_field
    @property
    def full_name(self) -> str:
        full_name = f"{self.first_name} {self.middle_name + ' ' if self.middle_name else ''}{self.last_name}"
        return full_name.title().strip()

    # def has_role(self, role: RoleChoicesSchema) -> bool:
    #     return self.role.value == role.value


    