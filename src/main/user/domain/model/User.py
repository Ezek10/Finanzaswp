from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.UserType import UserType


class User(BaseModel):
    id: str
    name: str
    type: UserType
    company: Optional[str]
    contact: Optional[str]
