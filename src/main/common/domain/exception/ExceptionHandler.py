from fastapi import Request
from fastapi.responses import JSONResponse

from src.main.common.domain.exception.ApplicationException import ApplicationException
from src.main.user.domain.exceptions import (
    UserAlreadyExistException,
    UserNotFoundException,
)


def ProcessException(request: Request, exception: Exception) -> JSONResponse:
    try:
        raise exception
    except UserNotFoundException as exc:
        print(exc)
        return JSONResponse(
            status_code=404, content="Not Found {}".format(request._body)
        )
    except UserAlreadyExistException as exc:
        print(exc)
        return JSONResponse(status_code=400, content="")
    except ApplicationException as exc:
        print(exc.args)
        return JSONResponse(status_code=500, content="Application Exception")
    except Exception as exc:
        print(exc.args)
        return JSONResponse(status_code=500, content=exc.args)
