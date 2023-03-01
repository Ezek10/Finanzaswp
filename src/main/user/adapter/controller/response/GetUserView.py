from typing import Optional

from pydantic import BaseModel


class GetUserView(BaseModel):
    id: str
    name: str
    company: Optional[str]
    contact: Optional[str]
