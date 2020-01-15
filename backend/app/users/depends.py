from fastapi import Depends, Header, HTTPException
from firebase_admin import auth as firebase_auth

from app.models import User
from app.users.schemes import FirebaseToken


def get_token(authorization: str = Header(None)) -> FirebaseToken:
    if authorization is None:
        raise HTTPException(status_code=401, detail='認証情報がありません')
    token = authorization.split(' ')[-1]
    try:
        token_dict = firebase_auth.verify_id_token(token)
        return FirebaseToken(**token_dict)
    except firebase_auth.InvalidIdTokenError as e:
        raise HTTPException(status_code=401, detail='トークンが不正です')


async def get_user(token: FirebaseToken = Depends(get_token)) -> User:
    firebase_user = firebase_auth.get_user(token.uid)
    user, _ = await User.get_or_create(None, defaults=dict(
        name=firebase_user.display_name,
        screen_name=firebase_user._data.get('screenName'),
        photo_url=firebase_user.photo_url,
    ), uid=token.uid)
    return user
