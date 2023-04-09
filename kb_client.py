from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def kb_client():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("/Works")
    kb.add(b1)
    return kb
