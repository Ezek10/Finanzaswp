from src.main.user.usecase.CreateUserUseCase import CreateUserUseCase
from src.tests.user.domain.port.command.UserCommandMother import UserCommandMother


def test_CreateUserUseCase():
    usecase = CreateUserUseCase()
    command = UserCommandMother().companyCommand()
    response = usecase.execute(command)
    assert response is None
