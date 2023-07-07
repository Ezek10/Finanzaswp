from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User


class Category(BaseModel):
    id: int
    name: str
    user: User
    parent: Optional('Category')
