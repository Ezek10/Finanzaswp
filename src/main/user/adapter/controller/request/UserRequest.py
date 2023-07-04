from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User
from src.main.user.domain.enums.UserType import UserType

class userContactRequest(BaseModel):
    email: Optional[str]
    linkedin: Optional[str]
    phone: Optional[int]

class UserRequest(BaseModel):
    name: str
    company: Optional[str]
    contact: userContactRequest
    
    def toDomain(self):
        return User(
            id = self.name,
            name = self.name,
            company=self.company,
            contact=self.contact,
            type=UserType.PJ if self.company is not None else UserType.PF,
        )
