from src.main.user.domain.model import User
from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserAlreadyExistException import UserAlreadyExistException


class CreateUserUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, user: User) -> None:
        if self.userRepository.fetch(user.id) is None:
            self.userRepository.create(user)
        else:
            raise UserAlreadyExistException(user)
