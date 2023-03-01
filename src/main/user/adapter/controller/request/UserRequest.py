from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.port.command.UserCommand import UserCommand


class UserRequest(BaseModel):
    id: str
    name: str
    company: Optional[str]
    contact: Optional[str]
    
    def toCommand(self):
        return UserCommand(
            id = self.id,
            name = self.name,
            company=self.company,
            contact=self.contact
        )
