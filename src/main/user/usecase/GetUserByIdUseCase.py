from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserNotFoundException import UserNotFoundException


class GetUserByIdUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, userId: str) -> None:
        if user := self.userRepository.fetch(userId) is not None:
            return user
        else:
            raise UserNotFoundException(userId)
