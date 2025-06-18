from fastapi import Request
from fastapi.responses import JSONResponse

from src.main.adapter.whatsapp.whatsapp import send_message
from src.main.domain.exceptions.base_exception import ApplicationException


def ProcessException(request: Request, exception: Exception) -> JSONResponse:
    try:
        raise exception

    except ApplicationException as ex:
        print(f"ApplicationException: {ex.phone} - {ex.args[0]}")
        send_message(ex.phone, ex.args[0])
        return JSONResponse(status_code=200, content="")

    except Exception as ex:
        print(f"ERROR {ex}")
        return JSONResponse(status_code=500, content="Internal Server Error")
