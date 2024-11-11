from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from .operations.keyboard_operations import KeyboardOperations

class Menu(KeyboardOperations):

    async def start(self):
        buttons_dict = {
            "Проверить модель на BLEU": "bleu",
            "Пообщаться с моделью LLM": "llm"
        }

        keyboard = await self.create_base_keyboard(buttons=buttons_dict)

        return keyboard