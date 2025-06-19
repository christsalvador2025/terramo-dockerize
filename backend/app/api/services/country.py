from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.logging import get_logger
from backend.app.models.country.models import Country
from backend.app.models.country.schema import (
    CountryCreateSchema,
    CountryReadSchema,
    CountryUpdateSchema,
)

logger = get_logger()


async def get_all_countries(session: AsyncSession) -> list[Country]:
    try:
        statement = select(Country)
        result = await session.exec(statement)
        countries = list(result.all())
        return countries
    except Exception as e:
        logger.error(f"Failed to retrieve countries: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Failed to get all countries"},
        )


