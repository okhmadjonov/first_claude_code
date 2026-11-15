from fastapi import FastAPI

from app.core.config import settings
from app.modules.notes.router import router as notes_router

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(notes_router)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}