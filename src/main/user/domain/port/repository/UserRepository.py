from abc import ABC, abstractmethod

from src.main.user.domain.model.User import User


class UserRepository(ABC):
    @abstractmethod
    def fetch(self, userId: str) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass
