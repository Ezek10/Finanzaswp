from src.main.domain.exceptions.base_exception import ApplicationException


class AccountNotFound(ApplicationException):
    """Exception to use when an account is not found in database"""

    def __init__(self, account: str, phone: str) -> None:
        message = f"Account {account} not found"
        super().__init__(phone, message)
