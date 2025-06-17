from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.api.routes.auth.deps import CurrentUser
from backend.app.api.services.company import get_all_companies
from backend.app.core.db import get_session
from backend.app.core.logging import get_logger
from backend.app.company.schema import CompanyReadSchema

logger = get_logger()
router = APIRouter(prefix="/companies")


@router.get(
    "/all",
    response_model=list[CompanyReadSchema],
    status_code=status.HTTP_200_OK,
    description="Get all companies for the authenticated user",
)
async def list_next_of_kins(
    current_user: CurrentUser, session: AsyncSession = Depends(get_session)
) -> list[CompanyReadSchema]:
    try:
        companies = await get_all_companies()
        return companies
    except HTTPException as http_ex:

        raise http_ex
    except Exception as e:
        logger.error(
            f"Failed to retrieve companies with error: {str(e)}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "status": "error",
                "message": "Failed to retrieve companies",
                "action": "Please try again later",
            },
        )
