from fastapi import APIRouter, Request, status

from src.main.common.domain.authorization.adminAuth import AdminAuthorization
from src.main.user.adapter.controller.request.UserRequest import UserRequest
from src.main.user.adapter.controller.mapper.mapperToView import mapper
from src.main.user.usecase.CreateUserUseCase import CreateUserUseCase
from src.main.user.usecase.GetUserByIdUseCase import GetUserByIdUseCase
from src.main.user.usecase.UpdateUserUseCase import UpdateUserUseCase
from src.main.user.usecase.GetAllUsersUseCase import GetAllUsersUseCase

router = APIRouter(prefix="/user")


@router.post("")
async def createUser(user: UserRequest):
    CreateUserUseCase().execute(user.toDomain())
    return status.HTTP_200_OK


@router.get("/{userId}")
async def getUser(userId: str):
    user = GetUserByIdUseCase().execute(userId)
    return mapper().toGetUserView(user)


@router.get("")
@AdminAuthorization
async def getAllUsers(request: Request):
    users = GetAllUsersUseCase().execute()
    return mapper().toGetAllUsersView(users)


@router.put("")
async def updateUser(user: UserRequest):
    UpdateUserUseCase().execute(user.toDomain())
    return status.HTTP_201_CREATED
