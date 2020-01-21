from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.models import User
from app.depends import get_db
from app.users.depends import get_user

router = APIRouter()


@router.get('')
async def index(n: str, db: Session = Depends(get_db)) -> dict:
    user = db.query(User).filter(User.screen_name == n).first()
    if user is None:
        raise HTTPException(status_code=404, detail='ユーザーが存在しません')
    return {'user': user.json()}


@router.get('/all')
async def all(db: Session = Depends(get_db)) -> dict:
    users = db.query(User).all()
    return {'users': [user.json() for user in users]}


@router.get('/me')
async def me(user: User = Depends(get_user)) -> dict:
    return user.json()
