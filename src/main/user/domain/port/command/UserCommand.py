from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User
from src.main.user.domain.model.UserType import UserType


class UserCommand(BaseModel):
    id: str
    name: str
    company: Optional[str]
    contact: Optional[str]

    def toDomain(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            company=self.company,
            contact=self.contact,
            type=UserType.PJ if self.company is not None else UserType.PF,
        )
