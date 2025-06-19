import os

from requests import request

from src.main.domain.schema.account import ListAccounts
from src.main.domain.schema.category import ListCategories
from src.main.domain.schema.transaction import ListTransactions


def send_reaction(phone: str, message_id: str, reaction: str):
    print("Sending Reaction to WhatsApp")
    auth = os.environ["AUTH"]
    facebook_ver = os.environ["FACEBOOK_VER"]
    phone_id = os.environ["PHONE_ID"]
    model = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "reaction",
        "reaction": {"message_id": message_id, "emoji": reaction},
    }
    url = f"https://graph.facebook.com/{facebook_ver}/{phone_id}/messages"
    header = {
        "Authorization": auth
    }
    response = request(method="post", url=url, headers=header, json=model)
    print(response, response.content)

def send_message(
    phone, message: str | ListTransactions | ListAccounts | ListCategories
):
    print("Sending Message to WhatsApp")
    auth = os.environ["AUTH"]
    facebook_ver = os.environ["FACEBOOK_VER"]
    phone_id = os.environ["PHONE_ID"]
    message = message_to_whatsapp_view(message)
    model = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {"body": message},
    }
    url = f"https://graph.facebook.com/{facebook_ver}/{phone_id}/messages"
    header = {
        "Authorization": auth
    }
    response = request(method="post", url=url, headers=header, json=model)
    print(response, response.content)


def message_to_whatsapp_view(message):
    if isinstance(message, ListAccounts):
        whatsapp_view = "Cuentas:\n"
        iterable = message.accounts
    elif isinstance(message, ListCategories):
        whatsapp_view = "Categorias:\n"
        iterable = message.categories
    elif isinstance(message, ListTransactions):
        whatsapp_view = "Transacciones:\n"
        iterable = message.transactions
    elif isinstance(message, str):
        return message
    for attr in iterable:
        whatsapp_view += attr.model_dump() + "\n"
    return whatsapp_view
