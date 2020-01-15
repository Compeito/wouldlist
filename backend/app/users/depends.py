import tortoise
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
    try:
        return await User.get(uid=token.uid)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(status_code=401, detail='ユーザーが存在しません')
