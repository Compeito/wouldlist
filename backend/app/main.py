import firebase_admin
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import settings
from app.models import Base
from app.db import engine
from app.users.routers import router as users_router
from app.items.routers import router as items_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

firebase_app = firebase_admin.initialize_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix='/users')
app.include_router(items_router, prefix='/items')
