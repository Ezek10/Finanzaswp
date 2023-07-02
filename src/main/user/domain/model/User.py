from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.enums.UserType import UserType


class UserContact(BaseModel):
    email: Optional[str]
    linkedin: Optional[str]
    phone: Optional[int]

class User(BaseModel):
    id: str
    name: str
    type: UserType
    company: Optional[str]
    contact: UserContact
