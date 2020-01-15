import firebase_admin
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.starlette import register_tortoise

from app import settings
from app.users.routers import router as users_router

app = FastAPI()

firebase_app = firebase_admin.initialize_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, settings.DB_CONFIG, generate_schemas=True)

app.include_router(users_router, prefix='/users', tags=['users api'])
