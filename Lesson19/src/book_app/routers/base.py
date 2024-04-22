from fastapi import APIRouter
from src.book_app.routers.book_router import router as book_router

router = APIRouter(
    prefix="/books",
    tags=["Booking"]
)

router.include_router(book_router)
