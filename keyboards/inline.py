from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_markup() -> InlineKeyboardButton:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Yosh gvardiyachi", callback_data="young_gvadiyachi"))
    kb.add(InlineKeyboardButton(text="Yoshlar va Qonun", callback_data="yoshlar_va_qonun"))
    kb.add(InlineKeyboardButton(text="Shunqorlar", callback_data="shunqorlar"))
    kb.adjust(1)
    return kb.as_markup()
