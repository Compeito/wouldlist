from fastapi import Depends, Query
from fastapi.routing import APIRouter
from firebase_admin import auth as firebase_auth
from starlette.requests import Request

from app.models import User
from app.users.depends import get_token
from app.users.schemes import FirebaseToken

router = APIRouter()


@router.post("/join")
async def join(
    token: dict = Depends(get_token),
    access_token: str = Query(None, alias='accessToken'),
    secret: str = Query(None),
):
    user = await User.create()
    return {"user": str(user)}


@router.get('/me')
async def me(request: Request, token: FirebaseToken = Depends(get_token)):
    import logging
    logger = logging.getLogger('uvicorn')
    logger.info(token)
    logger.info(firebase_auth.get_user(token.uid))
    return token
