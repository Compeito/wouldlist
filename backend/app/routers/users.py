from fastapi.routing import APIRouter
from starlette.requests import Request

from ..models import User

router = APIRouter()


@router.get("")
async def index(_: Request):
    users = await User.all()
    return {"users": [str(user) for user in users]}


@router.post("/add")
async def add(_: Request, username: str):
    user = await User.create(username=username)
    return {"user": str(user)}
