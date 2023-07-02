from fastapi import APIRouter, Request, status

from src.main.common.domain.authorization.adminAuth import AdminAuthorization
from src.main.user.adapter.controller.request.UserRequest import UserRequest
from src.main.user.adapter.controller.mapper.mapperToView import mapper
from src.main.user.usecase.CreateUserUseCase import CreateUserUseCase
from src.main.user.usecase.GetUserByIdUseCase import GetUserByIdUseCase
from src.main.user.usecase.UpdateUserUseCase import UpdateUserUseCase

router = APIRouter()


@router.get("/")
async def home():
    return status.HTTP_200_OK


@router.post("/user")
async def createUser(user: UserRequest):
    CreateUserUseCase().execute(user.toDomain())
    return status.HTTP_200_OK


@router.get("/user/{userId}")
async def getUser(userId: str):
    user = GetUserByIdUseCase().execute(userId)
    return mapper().toGetUserView(user)


@router.put("/user")
async def updateUser(user: UserRequest):
    UpdateUserUseCase().execute(user.toDomain())
    return status.HTTP_201_CREATED
