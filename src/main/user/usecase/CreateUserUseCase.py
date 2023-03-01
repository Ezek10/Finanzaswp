from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.exceptions.UserAlreadyExistException import UserAlreadyExistException
from src.main.user.domain.port.command.UserCommand import UserCommand


class CreateUserUseCase:
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self, command: UserCommand) -> None:
        user = command.toDomain()
        if self.userRepository.fetch(user.id) is None:
            self.userRepository.create(user)
        else:
            raise UserAlreadyExistException(user)
