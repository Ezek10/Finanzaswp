from src.main.user.domain.port.command.UserCommand import UserCommand


class UserCommandMother:
    def companyCommand(self):
        return UserCommand(
            id=123,
            name="name",
            company="company",
            contact="name@company.com"
        )

    def personCommand(self):
        return UserCommand(id=123, name="name")
