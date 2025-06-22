from datetime import datetime

from fastapi import Depends, Request, Response, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.main.adapter.controller.request.whats_app_request import WPRequest
from src.main.adapter.repository.config import get_db
from src.main.domain.exceptions.handler import ProcessException
from src.main.usecases.process_message_use_case import ProcessMessageUseCase

router = APIRouter(prefix="/whats_app")


@router.get("")
async def verification(request: Request):
    print(f"Query params: {request.query_params}")
    response = request.query_params["hub.challenge"]
    return Response(status_code=200, content=response)


@router.post("")
async def read_message(request: dict, background_tasks: BackgroundTasks, session = Depends(get_db)):
    def task(request: dict, session):
        try:
            print(f"Request: {request}")
            request_parsed = WPRequest(**request)
            message = request_parsed.entry[0].changes[0].value.messages[0]
            message_id = message.id
            phone = message.from_
            timestamp = int(message.timestamp)
            body = message.text.body
            date = datetime.fromtimestamp(timestamp)
            ProcessMessageUseCase(session).execute(phone=phone, message=body, date=date, message_id=message_id)
        except Exception as ex:
            ProcessException(request, ex)
    background_tasks.add_task(task, request, session)
    return JSONResponse(status_code=200, content="")
