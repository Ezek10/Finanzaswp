from fastapi import Request
from fastapi.responses import JSONResponse

from src.main.adapter.whatsapp.whatsapp import send_message
from src.main.domain.exceptions.base_exception import ApplicationException


def ProcessException(request: Request, exception: Exception) -> JSONResponse:
    try:
        raise exception

    except ApplicationException as ex:
        print(f"ApplicationException: {ex.phone} - {ex.args}")
        send_message(ex.phone, ex.args[0])

    except Exception as ex:
        print(f"Error - Exception: {ex.args}")
