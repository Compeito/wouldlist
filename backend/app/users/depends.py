from fastapi import Depends, Header, HTTPException
from firebase_admin import auth as firebase_auth

from app.users.schemes import FirebaseToken


def get_token(authorization: str = Header(None)) -> FirebaseToken:
    token = authorization.split(' ')[-1]
    try:
        token_dict = firebase_auth.verify_id_token(token)
        return FirebaseToken(**token_dict)
    except firebase_auth.InvalidIdTokenError as e:
        raise HTTPException(status_code=403, detail='トークンが不正です')


def get_user(token: FirebaseToken = Depends(get_token)):
    pass
