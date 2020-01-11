import logging
import os

from authlib.integrations.starlette_client import OAuth, RemoteApp
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from tortoise.contrib.starlette import register_tortoise

from . import settings
from .routers import users

logging.basicConfig(format='%(levelname)s: <%(pathname)s:%(lineno)d>\n> %(message)s')

oauth = OAuth()
# http://docs.authlib.org/en/latest/client/frameworks.html
oauth.register(
    name='twitter',
    client_id=os.environ['TWITTER_CLIENT_KEY'],
    client_secret=os.environ['TWITTER_CLIENT_SECRET'],
    request_token_url='https://api.twitter.com/oauth/request_token',
    request_token_params=None,
    access_token_url='https://api.twitter.com/oauth/access_token',
    access_token_params=None,
    authorize_url='https://api.twitter.com/oauth/authenticate',
    authorize_params=None,
    api_base_url='https://api.twitter.com/1.1/',
    client_kwargs=None,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, settings.DB_CONFIG, generate_schemas=True)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.include_router(users.router, prefix='/users', tags=['users api'])


@app.get('/login')
async def login(request: Request):
    client: RemoteApp = oauth.create_client('twitter')
    redirect_uri = f'http://localhost:3000/login/callback'
    auth_url = await client.create_authorization_url(redirect_uri)
    client.save_authorize_data(request, redirect_uri=redirect_uri, **auth_url)
    return auth_url


@app.post('/login/callback')
async def authorize(request: Request, oauth_verifier: str, oauth_token: str):
    client: RemoteApp = oauth.create_client('twitter')
    client.access_token_params = {
        'verifier': oauth_verifier,
    }
    try:
        token = await client.authorize_access_token(request)
        resp = await client.get('account/verify_credentials.json', token=token)
        return resp.json()
    except Exception as e:
        return {'error': str(e)}
