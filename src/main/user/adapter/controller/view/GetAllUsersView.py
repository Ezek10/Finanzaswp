from pydantic import BaseModel

from src.main.user.adapter.controller.view.GetUserView import GetUserView

class GetAllUsersView(BaseModel):
    users: list = list()
