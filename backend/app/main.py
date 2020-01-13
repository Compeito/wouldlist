import logging

import firebase_admin
from fastapi import FastAPI, Header, Depends
from firebase_admin import auth as firebase_auth
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from tortoise.contrib.starlette import register_tortoise

from . import settings
from .routers import users

app = FastAPI()
logger = logging.getLogger('uvicorn')

firebase_app = firebase_admin.initialize_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, settings.DB_CONFIG, generate_schemas=True)
app.include_router(users.router, prefix='/users', tags=['users api'])


def get_user(authorization: str = Header(None)):
    token = authorization.split(' ')[-1]
    try:
        return firebase_auth.verify_id_token(token)
    except Exception as e:
        return {'error': str(type(e)) + ': ' + str(e)}


@app.get('/me')
async def login(request: Request, user: dict = Depends(get_user)):
    return user
