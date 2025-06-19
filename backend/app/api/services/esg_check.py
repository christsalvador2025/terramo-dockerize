from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.logging import get_logger
from backend.app.models.esg_check.models import EsgCheck
from backend.app.models.esg_check.schema import (
    EsgCheckCreateSchema,
    EsgCheckReadSchema,
    EsgCheckUpdateSchema,
)

logger = get_logger()


async def get_all_esg_checks(session: AsyncSession) -> list[EsgCheck]:
    try:
        statement = select(EsgCheck)
        result = await session.exec(statement)
        esg_checks = list(result.all())
        return esg_checks
    except Exception as e:
        logger.error(f"Failed to retrieve esg_checks: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Failed to get all esg_checks"},
        )


