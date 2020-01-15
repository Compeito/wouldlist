from fastapi import Depends
from fastapi.routing import APIRouter

from app.models import User
from app.users.depends import get_user

router = APIRouter()

@router.get('/me')
async def me(user: User = Depends(get_user)) -> dict:
    return user.json()
