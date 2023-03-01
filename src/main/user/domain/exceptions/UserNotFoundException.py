from src.main.common.domain.exception.ApplicationException import ApplicationException


class UserNotFoundException(ApplicationException):
    def __init__(self, userId: str) -> None:
        message = f"User with id {userId} do not exist!"
        super().__init__(message)
