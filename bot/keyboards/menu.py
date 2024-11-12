from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from .operations.keyboard_operations import KeyboardOperations

class Menu:
    @staticmethod
    async def start():
        buttons_dict = {
            "BLEU-metric": "bleu",
            "LLM-generation": "llm"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard
