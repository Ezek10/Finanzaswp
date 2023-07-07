from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User

class userContactRequest(BaseModel):
    email: Optional[str]
    phone: int

class UserRequest(BaseModel):
    name: Optional[str]
    contact: userContactRequest
    
    def toDomain(self):
        return User(
            id = self.contact.phone,
            name = self.name,
            contact=self.contact,
        )
