from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.repository.repository_impl import Database
from src.main.domain.schema.account import Account
from src.main.domain.schema.user import User


class AccountUseCase:
    def __init__(self, session):
        self.session = session

    def create(self, phone: str, account: Account):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print(f"Creating Account: {account.name}")
        Database(self.session).create_account(phone=phone, account=account)

    def delete(self, phone: str, account: Account):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print(f"Deleting Account: {account.name}")
        Database(self.session).delete_account(phone=phone, account=account)

    def get_all(self, phone: str):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_accounts_with_phone(phone)
