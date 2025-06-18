from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.logging import get_logger
from backend.app.company.models import Company
from backend.app.company.schema import (
    CompanyCreateSchema,
    CompanyReadSchema,
    CompanyUpdateSchema,
)

logger = get_logger()


async def get_all_companies(session: AsyncSession) -> list[Company]:
    try:
        statement = select(Company)
        result = await session.exec(statement)
        companies = list(result.all())
        return companies
    except Exception as e:
        logger.error(f"Failed to retrieve companies: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Failed to get all companies"},
        )


