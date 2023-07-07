from typing import Optional

from pydantic import BaseModel


class UserContact(BaseModel):
    email: Optional[str]
    phone: int

class GetUserView(BaseModel):
    id: str
    name: Optional[str]
    contact: UserContact
