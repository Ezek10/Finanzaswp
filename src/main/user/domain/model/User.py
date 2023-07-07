from typing import Optional

from pydantic import BaseModel


class UserContact(BaseModel):
    email: Optional[str]
    phone: int

class User(BaseModel):
    id: str
    name: Optional[str]
    contact: UserContact
