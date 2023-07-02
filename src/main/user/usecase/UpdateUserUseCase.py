from src.main.user.domain.model import User
from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserNotFoundException import UserNotFoundException


class UpdateUserUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, user: User) -> None:
        if self.userRepository.fetch(user.id) is not None:
            self.userRepository.update(user)
        else:
            raise UserNotFoundException(user.id)
