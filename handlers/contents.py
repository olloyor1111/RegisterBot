from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import get_inline_markup

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Это текстовое сообщение!", reply_markup=get_inline_markup())

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер!")

@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это GIF!")