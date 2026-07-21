from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .config import settings
from .database import engine, Base
from .routers import auth, content, api_keys, payments

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes first
app.include_router(auth.router)
app.include_router(content.router)
app.include_router(api_keys.router)
app.include_router(payments.router)


@app.get("/health")
def health():
    return {"status": "healthy"}


# Serve frontend - registered last so API routes take priority
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
