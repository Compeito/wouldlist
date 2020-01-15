from fastapi import Depends, Body
from fastapi.routing import APIRouter
from firebase_admin import auth as firebase_auth

from app.models import User
from app.users.depends import get_token, get_user
from app.users.schemes import FirebaseToken

router = APIRouter()


@router.post("/join")
async def join(
    token: FirebaseToken = Depends(get_token),
    access_token: str = Body(None, alias='accessToken'),
    secret: str = Body(None),
):
    firebase_user = firebase_auth.get_user(token.uid)
    user, created = await User.get_or_create(None, defaults=dict(
        name=firebase_user.display_name,
        photo_url=firebase_user.photo_url,
        screen_name=firebase_user._data.get('screenName'),
        access_token=access_token,
        access_secret=secret,
    ), uid=token.uid)
    return {'user': user.json(), 'isCreated': created}


@router.get('/me')
async def me(user: User = Depends(get_user)):
    return user.json()
