from typing import Optional

from pydantic import BaseModel


class UserContact(BaseModel):
    email: Optional[str]
    linkedin: Optional[str]
    phone: Optional[int]

class GetUserView(BaseModel):
    id: str
    name: str
    company: Optional[str]
    contact: UserContact
