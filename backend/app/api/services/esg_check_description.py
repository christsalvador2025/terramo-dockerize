from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.logging import get_logger
from backend.app.models.esg_check_description.models import EsgCheckDescription
from backend.app.models.esg_check_description.schema import (
    EsgCheckDescriptionCreateSchema,
    EsgCheckDescriptionReadSchema,
    EsgCheckDescriptionUpdateSchema,
)

logger = get_logger()


async def get_all_esg_checks_descriptions(session: AsyncSession) -> list[EsgCheckDescription]:
    try:
        statement = select(EsgCheckDescription)
        result = await session.exec(statement)
        esg_checks_descriptions = list(result.all())
        return esg_checks_descriptions
    except Exception as e:
        logger.error(f"Failed to retrieve esg_checks_descriptions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Failed to get all esg_checks_descriptions"},
        )


