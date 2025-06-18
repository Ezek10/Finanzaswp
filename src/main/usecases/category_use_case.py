from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.repository.repository_impl import Database
from src.main.domain.schema.category import Category
from src.main.domain.schema.user import User


class CategoryUseCase:
    def __init__(self, session):
        self.session = session

    def create(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print(f"Creating Category: {category.name}")
        Database(self.session).create_category(phone=phone, category=category)

    def delete(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print(f"Deleting Category: {category.name}")
        Database(self.session).delete_category(phone=phone, category=category)

    def get_all(self, phone: str):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_categories_with_phone(phone=phone)

    def get_one(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_categories_with_phone(phone=phone)
