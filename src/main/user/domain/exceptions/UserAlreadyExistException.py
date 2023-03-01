from src.main.common.domain.exception.ApplicationException import ApplicationException
from src.main.user.domain.model.User import User


class UserAlreadyExistException(ApplicationException):
    def __init__(self, user: User) -> None:
        message = f"User with id {user.id} already exist!"
        super().__init__(message)
