from src.main.user.adapter.repository.InMemoryUserRepository import InMemoryUserRepository
from src.main.user.domain.model.User import User

class GetAllUsersUseCase():
    def __init__(self) -> None:
        self.userRepository = InMemoryUserRepository()

    def execute(self) -> list[User]:
        return self.userRepository.getAll()
