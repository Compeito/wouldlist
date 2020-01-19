from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
import tortoise.exceptions

from app.models import User
from app.users.depends import get_user

router = APIRouter()


@router.get('')
async def index(n: str) -> dict:
    try:
        user = await User.get(screen_name=n)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(status_code=404, detail='ユーザーが存在しません')
    return {'user': user.json()}


@router.get('/all')
async def all() -> dict:
    users = await User.all()
    return {'users': [user.json() for user in users]}


@router.get('/me')
async def me(user: User = Depends(get_user)) -> dict:
    return user.json()
