from datetime import datetime
from sqlalchemy.orm import Session

from src.main.usecases.account_use_case import AccountUseCase
from src.main.usecases.category_use_case import CategoryUseCase
from src.main.usecases.transaction_use_case import TransactionUseCase
from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.whatsapp.whatsapp import send_message, send_reaction
from src.main.domain.schema.account import Account
from src.main.domain.schema.category import Category
from src.main.domain.schema.transaction import Transaction
from src.main.domain.schema.user import User


class ProcessMessageUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, phone: str, message: str, message_id: str, date: datetime = datetime.now()):
        try:
            words_spend = ["gaste", "gasté"]
            words_configuration = ["configurar"]
            words_create = ["crear", "definir"]
            words_ingreso = ["ingreso"]
            words_delete = ["borrar"]
            words_transfer = ["transferi", "transferí", "retire"]
            words_list = ["listar", "traer", "mostrar"]
            message = message.lower()
            print(f"Phone: {phone}")
            print(f"Message: {message}")
            if self._words_in_message(words_configuration, message):
                print("Processing Configuration")
                message_to_send = self._proccess_configuration(phone, message)
            elif self._words_in_message(words_create, message):
                print("Processing create")
                message_to_send = self._proccess_create(phone, message)
            elif self._words_in_message(words_ingreso, message):
                print("Processing ingreso")
                message_to_send = self._proccess_ingreso(phone, message, date)
            elif self._words_in_message(words_transfer, message):
                print("Processing transfer")
                message_to_send = self._proccess_transfer(phone, message, date)
            elif self._words_in_message(words_spend, message):
                print("Processing spend")
                message_to_send = self._proccess_spend(phone, message, date)
            elif self._words_in_message(words_list, message):
                print("Processing list")
                message_to_send = self._proccess_list(phone, message)
            elif self._words_in_message(words_delete, message):
                print("Processing delete")
                message_to_send = self._proccess_delete(phone, message)
            else:
                print("Processing help")
                message_to_send = self._proccess_help()
            if message_to_send is not None:
                send_message(phone, message_to_send)
            send_reaction(phone, message_id, "✅")
            return message_to_send
        except Exception as e:
            print(f"Error processing message: {e}")
            send_reaction(phone, message_id, "❌")
            return f"Error al procesar el mensaje: {e}"

    def _proccess_help(self):
        message = """Hola, si no sabes que quieres pedirme, prueba con:
    - Crear cuenta tu_cuenta
    - Crear categoria tu_categoria
    - Gaste 300 por tu_categoria en tu_cuenta
    - Ingreso 300 por tu_categoria en tu_cuenta
    - Transferi 300 desde tu_cuenta_origen hacia tu_cuenta_destino
    - Listar categorias
    - Listar cuentas
    - Listar transacciones
    - Listar transacciones con categoria tu_categoria
    - Listar transacciones con cuenta tu_cuenta
    - Configurar email 'email@example.com'
    - Configurar nombre 'nombre_de_usuario'

Recuerda que las *Cuentas* son donde tenes tu dinero, sea el nombre de un banco o tu misma billetera.
Las *Categorias* son como vos queres organizar tus gastos como alquiler, comida, etc.
Los nombres de las cuentas y categorias no pueden tener espacios, pero si guiones bajos o guiones medios.
Si tu mensaje se proceso bien se te reaccionara con un ✅, si hubo un error se te reaccionara con un ❌.
"""
        return message

    def _proccess_spend(self, phone: str, message: str, date: datetime):
        spend, amount, forr, category, inn, account = message.split(" ")
        amount = int(amount)
        category = Category(name=category)
        account = Account(name=account)
        transaction = Transaction(
            amount=-amount, created_at=date, category=category, account=account
        )
        return TransactionUseCase(self.session).create(phone=phone, transaction=transaction)

    def _proccess_delete(self, phone, message: str):
        delete, attr, name = message.split(" ")
        if attr in {"transaccion", "transacción"}:
            return TransactionUseCase(self.session).delete_with_id(phone, name)
        elif attr == "cuenta":
            account = Account(name=name)
            return AccountUseCase(self.session).delete(phone, account)
        elif attr in {"categoria", "categoría"}:
            category = Category(name=name)
            return CategoryUseCase(self.session).delete(phone, category)

    def _proccess_list(self, phone: str, message: str):
        list, *attr = message.split(" ")
        if attr[0] == "transacciones":
            if "categoria" in attr or "categoría" in attr:  # list transactions with category xxx
                return TransactionUseCase(self.session).get_filtered_by_category(phone, attr[3])
            elif "cuenta" in attr:
                return TransactionUseCase(self.session).get_filtered_by_account(phone, attr[3])
            else:
                return TransactionUseCase(self.session).get_all(phone)
        elif attr[0] == "cuentas":
            return AccountUseCase(self.session).get_all(phone)
        elif attr[0] == "categorias":
            return CategoryUseCase(self.session).get_all(phone)

    def _proccess_configuration(self, phone: str, message: str):
        if "email" in message:
            configure, email, address = message.split(" ")
            user = User(phone=phone, email=address)
        elif "nombre" in message:
            configure, name, user_name = message.split(" ")
            user = User(phone=phone, name=user_name)
        else:
            return
        return UserUseCase(self.session).update(user=user)

    def _proccess_create(self, phone: str, message: str):
        create, attr, name = message.split(" ")
        if attr == "cuenta":
            account = Account(name=name)
            return AccountUseCase(self.session).create(phone=phone, account=account)
        elif attr in {"categoria", "categoría"}:
            category = Category(name=name)
            return CategoryUseCase(self.session).create(phone=phone, category=category)

    def _proccess_ingreso(self, phone: str, message: str, date: datetime):
        ingreso, amount, forr, category, inn, account = message.split(" ")
        account = Account(name=account)
        category = Category(name=category)
        transaction = Transaction(
            amount=amount, created_at=date, category=category, account=account
        )
        return TransactionUseCase(self.session).create(phone=phone, transaction=transaction)

    def _proccess_transfer(self, phone: str, message: str, date: datetime):
        transfer, amount, fromm, account_origin, to, account_destiny = message.split(
            " "
        )
        account_origin = Account(name=account_origin)
        account_destiny = Account(name=account_destiny)
        category = Category(name="transfer")
        transaction_origin = Transaction(
            amount=-amount,
            created_at=date,
            description=f"Transfer from {account_origin} to {account_destiny}",
            account=account_origin,
            category=category,
        )
        transaction_destiny = Transaction(
            amount=amount,
            created_at=date,
            description=f"Transfer from {account_origin} to {account_destiny}",
            account=account_destiny,
            category=category,
        )
        TransactionUseCase(self.session).create(
            phone=phone,
            transaction=transaction_origin,
        )
        TransactionUseCase(self.session).create(
            phone=phone,
            transaction=transaction_destiny,
        )

    def _words_in_message(self, words: list[str], message: str):
        for word in words:
            if word in message:
                return True
        return False
