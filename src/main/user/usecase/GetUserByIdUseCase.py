from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserNotFoundException import UserNotFoundException
from src.main.user.domain.model.User import User


class GetUserByIdUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, userId: str) -> User:
        if user := self.userRepository.fetch(userId) is not None:
            return user
        else:
            raise UserNotFoundException(userId)
