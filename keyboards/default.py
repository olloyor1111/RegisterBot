from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb_markup() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="✅ Ha"))
    kb.add(KeyboardButton(text="❌ Yo'q"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)


def register_markup() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="👤 Ro'yxatdan o'tish"))
    return kb.as_markup(resize_keyboard=True)

def get_choice_markup() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="O'quvchi"))
    kb.add(KeyboardButton(text="Talaba"))
    kb.add(KeyboardButton(text="Uyushmagan yosh"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

def get_phone_markup() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="📱 Telefon raqam ulashish", request_contact=True))
    return kb.as_markup(resize_keyboard=True)

def get_confirm_markup() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="✅ Ha"))
    kb.add(KeyboardButton(text="❌ Yo'q"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
