from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.main.user.domain.model.User import User


class Transaction(BaseModel):
    id: int
    amount: float
    categoryid: int
    date: datetime
    description: Optional[str]
    user: User
    accountid: int
