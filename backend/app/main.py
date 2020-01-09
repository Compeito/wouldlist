import os
import logging

from authlib.integrations.starlette_client import OAuth, RemoteApp
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from tortoise.contrib.starlette import register_tortoise

from .models import Users

logging.basicConfig(format='%(levelname)s: <%(pathname)s:%(lineno)d>\n> %(message)s')

DB_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'db',
                'port': '3306',
                'user': 'root',
                'password': os.environ['MYSQL_ROOT_PASSWORD'],
                'database': 'wouldlist',
            }
        },
    },
    'apps': {
        'models': {
            'models': ['app.main'],
            'default_connection': 'default',
        }
    }
}
SECRET_KEY = os.environ['SECRET_KEY']

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
register_tortoise(app, DB_CONFIG, generate_schemas=True)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


@app.get("/users")
async def list_all(_: Request):
    users = await Users.all()
    return {"users": [str(user) for user in users]}


@app.post("/users/add")
async def add_user(_: Request, username: str):
    user = await Users.create(username=username)
    return {"user": str(user)}


@app.get('/login')
async def login(request: Request):
    client = oauth.create_client('twitter')
    redirect_uri = f'http://192.168.99.100/authorize'
    return await client.authorize_redirect(request, redirect_uri)


@app.get('/authorize')
async def authorize(request: Request):
    client: RemoteApp = oauth.create_client('twitter')
    client.access_token_params = {
        'verifier': request.query_params['oauth_verifier']
    }
    token = await client.authorize_access_token(request)
    resp = await client.get('account/verify_credentials.json', token=token)
    return resp.json()
