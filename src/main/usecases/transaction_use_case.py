from src.main.domain.schema.transaction import Transaction
from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.repository.repository_impl import Database
from src.main.domain.schema.account import Account
from src.main.domain.schema.category import Category
from src.main.domain.schema.user import User


class TransactionUseCase:
    def __init__(self, session):
        self.session = session

    def get_all(self, phone: str):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_transaction_with_phone(phone)

    def get_filtered_by_account(self, phone: str, account: Account):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_transaction_with_phone_and_account(
            phone=phone, account=account
        )

    def get_filtered_by_category(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        return Database(self.session).list_transaction_with_phone_and_category(
            phone=phone, category=category
        )

    def create(
        self,
        phone: str,
        transaction: Transaction,
    ):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print("Creating transaction")
        Database(self.session).create_transaction(phone=phone, transaction=transaction)

    def delete_with_id(
        self,
        phone: str,
        transaction_id: int,
    ):
        user = User(phone=phone)
        if Database(self.session).user_exist(user=user) is False:
            UserUseCase(self.session).create(user=user)
        print("Deleting transaction")
        Database(self.session).delete_transaction(phone=phone, transaction_id=transaction_id)
