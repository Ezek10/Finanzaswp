from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User


class Account(BaseModel):
    id: int
    currency: Optional[str]
    name: str
    user: User
