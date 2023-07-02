from src.main.user.adapter.controller.view.GetAllUsersView import GetAllUsersView
from src.main.user.adapter.controller.view.GetUserView import GetUserView, UserContact
from src.main.user.domain.model.User import User


class mapper:
    def toGetAllUsersView(self, users: list[User]) -> GetAllUsersView:
        return [self.toGetUserView(user) for user in users]

    def toGetUserView(self, user: User) -> GetUserView:
        return GetUserView(
            id=user.id,
            name=user.name,
            company=user.company,
            contact=UserContact(
                email=user.contact.email,
                linkedin=user.contact.linkedin,
                phone=user.contact.phone
            )
        )
