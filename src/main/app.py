from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.main.common.domain.exception.ExceptionHandler import ProcessException
from src.main.user.adapter.controller.UserController import router as userRouter

app = FastAPI()
app.include_router(userRouter)


@app.exception_handler(Exception)
def ExceptionsHandler(request: Request, exception: Exception) -> JSONResponse:
    return ProcessException(request, exception)
