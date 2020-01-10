from fastapi.routing import APIRouter
from starlette.requests import Request

from ..models import Users

router = APIRouter()


@router.get("")
async def index(_: Request):
    users = await Users.all()
    return {"users": [str(user) for user in users]}


@router.post("/add")
async def add(_: Request, username: str):
    user = await Users.create(username=username)
    return {"user": str(user)}
