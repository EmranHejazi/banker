from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.services.customer_service import CustomerService


router = APIRouter(prefix="/api/search")

class SearchRequest(BaseModel):
    search: Optional[str] = None
    filters: dict

@router.post("/")
async def search(req: SearchRequest):
    return await CustomerService.search(
        req.search,
        req.filters
    )
