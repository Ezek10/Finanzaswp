from src.main.domain.exceptions.base_exception import ApplicationException


class CategoryNotFound(ApplicationException):
    """Exception to use when a category is not found in database"""

    def __init__(self, category: str, phone: str) -> None:
        message = f"Category {category} not found"
        super().__init__(phone, message)
