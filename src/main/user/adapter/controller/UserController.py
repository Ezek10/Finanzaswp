from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.main.user.adapter.controller.request.UserRequest import UserRequest
from src.main.user.adapter.controller.response.GetUserView import GetUserView
from src.main.user.usecase.CreateUserUseCase import CreateUserUseCase
from src.main.user.usecase.GetUserByIdUseCase import GetUserByIdUseCase
from src.main.user.usecase.UpdateUserUseCase import UpdateUserUseCase

router = APIRouter()


@router.get("/")
async def home():
    return JSONResponse(status_code=200, content="Application UP!")


@router.post("/user")
async def createUser(user: UserRequest):
    CreateUserUseCase().execute(user.toCommand())
    return JSONResponse(status_code=200, content=None)


@router.get("/user/{userId}")
async def getUser(userId: str):
    user = GetUserByIdUseCase().execute(userId)
    return GetUserView(user)


@router.put("/user")
async def updateUser(user: UserRequest):
    UpdateUserUseCase().execute(user.toCommand())
    return JSONResponse(status_code=204)
