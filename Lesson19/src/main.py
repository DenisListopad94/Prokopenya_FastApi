from fastapi import FastAPI
from src.auth.routers.base import router as auth_router
from src.book_app.routers.base import router as book_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(auth_router)
app.include_router(book_router)

app.mount("/static", StaticFiles(directory="static"), name="static")




