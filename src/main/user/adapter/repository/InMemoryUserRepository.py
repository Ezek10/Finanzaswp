from main.user.domain.model.User import User
from main.user.domain.port.repository.UserRepository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def fetch(self, userId: str) -> User:
        return self._users.get(userId)

    def create(self, user: User) -> None:
        self._users[user.id] = user

    def update(self, user: User) -> None:
        self._users.get(user.id)
