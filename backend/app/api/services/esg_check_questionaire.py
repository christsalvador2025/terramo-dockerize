from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.logging import get_logger
from backend.app.models.esg_check_questionaire.models import EsgCheckQuestionaire
from backend.app.models.esg_check_questionaire.schema import (
    EsgCheckQuestionaireCreateSchema,
    EsgCheckQuestionaireReadSchema,
    EsgCheckQuestionaireUpdateSchema,
)

logger = get_logger()


async def get_all_esg_check_questionaires(session: AsyncSession) -> list[EsgCheckQuestionaire]:
    try:
        statement = select(EsgCheckQuestionaire)
        result = await session.exec(statement)
        esg_checks_questionaires = list(result.all())
        return esg_checks_questionaires
    except Exception as e:
        logger.error(f"Failed to retrieve esg_checks_questionaires: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Failed to get all esg_checks_questionaires"},
        )


