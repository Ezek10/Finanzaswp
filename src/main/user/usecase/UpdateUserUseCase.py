from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserNotFoundException import UserNotFoundException
from src.main.user.domain.port.command.UserCommand import UserCommand


class UpdateUserUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, command: UserCommand) -> None:
        user = command.toDomain()
        if self.userRepository.fetch(user.id) is not None:
            self.userRepository.update(user)
        else:
            raise UserNotFoundException(user.id)
