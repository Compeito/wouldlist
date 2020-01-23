from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.models import User, Item
from app.depends import get_db
from app.users.depends import get_user

router = APIRouter()


@router.get('')
async def index(uid: str, db: Session = Depends(get_db)) -> dict:
    item = db.query(Item).filter(Item.uid == uid).first()
    if item is None:
        raise HTTPException(status_code=404, detail='アイテムが存在しません')
    return {'item': item.json(('user',))}


@router.post('/create')
async def create(text: str, user: User = Depends(get_user), db: Session = Depends(get_db)) -> dict:
    item = Item(user=user, text=text)
    db.add(item)
    db.commit()
    db.refresh(item)
    return {'item': item.json()}


@router.delete('/delete')
async def delete(uid: str, user: User = Depends(get_user), db: Session = Depends(get_db)) -> dict:
    item = db.query(Item).filter(Item.uid == uid).first()
    if item is None:
        raise HTTPException(status_code=404, detail='アイテムが存在しません')

    if not item.user == user:
        raise HTTPException(status_code=403, detail='ユーザー情報が一致しません')

    db.delete(item)
    return {'success': True}
