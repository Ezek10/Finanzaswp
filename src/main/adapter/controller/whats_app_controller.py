from datetime import datetime

from fastapi import Depends, Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.main.adapter.controller.request.whats_app_request import WPRequest
from src.main.adapter.repository.config import get_db
from src.main.usecases.process_message_use_case import ProcessMessageUseCase

router = APIRouter(prefix="/whats_app")


@router.get("")
async def verification(request: Request):
    print(f"Query params: {request.query_params}")
    response = request.query_params["hub.challenge"]
    return Response(status_code=200, content=response)


@router.post("")
async def read_message(request: dict, session = Depends(get_db)):
    print(f"Request: {request}")
    try:
        request_parsed = WPRequest(**request)
    except Exception as e:
        return JSONResponse(status_code=422, content={"error": str(e)})
    message = request_parsed.entry[0].changes[0].value.messages[0]
    message_id = message.id
    phone = message.from_
    timestamp = int(message.timestamp)
    body = message.text.body
    date = datetime.fromtimestamp(timestamp)
    ProcessMessageUseCase(session).execute(phone=phone, message=body, date=date, message_id=message_id)
    return JSONResponse(status_code=200, content="")
