from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
import tortoise.exceptions

from app.models import User, Item
from app.users.depends import get_user

router = APIRouter()


@router.get('')
async def index(uid: str) -> dict:
    try:
        item = await Item.get(uid=uid)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(status_code=404, detail='アイテムが存在しません')
    return {'item': item.json()}


@router.post('/create')
async def create(text: str, user: User = Depends(get_user)) -> dict:
    item = await Item.create(user=user, text=text)
    return {'item': item.json()}


@router.delete('/delete')
async def delete(uid: str, user: User = Depends(get_user)) -> dict:
    try:
        item = await Item.get(uid=uid)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(status_code=404, detail='アイテムが存在しません')

    if not item.user == user:
        raise HTTPException(status_code=403, detail='ユーザー情報が一致しません')

    await item.delete()
    return {'item': item.json()}
