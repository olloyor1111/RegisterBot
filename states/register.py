from aiogram.fsm.state import State, StatesGroup

class RegisterStates(StatesGroup):
    fio = State()
    age = State()
    status = State()
    choice = State()
    phone_number = State()
    confirm = State()
