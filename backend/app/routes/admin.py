from fastapi import APIRouter
from ..services.age_service import AgeService

router = APIRouter(prefix="/api/admin")

@router.post("/update-age")
async def update_age():
    return await AgeService.update_age_if_needed()
