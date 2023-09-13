from aiogram.filters import CommandStart
from aiogram import Router, F, types
from extra import add_user_to_db
from keyboards.default import get_kb_markup, register_markup


router = Router()

@router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    try:
        add_user_to_db(telegram_id=telegram_id, first_name=first_name, last_name=last_name, username=username)
    except Exception as error:
        print(error)
    await message.answer(f"Assalomu alaykum {first_name} {last_name}!", reply_markup=register_markup())


