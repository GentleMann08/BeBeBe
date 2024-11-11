from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

class KeyboardOperations:

    @staticmethod
    async def create_base_keyboard(buttons: dict, interval: int = 1, count: int = 0, reply: bool = None, is_builder: bool = None):
        buttons_list = list()
        interval_count = 0

        if reply:
            keyboard = ReplyKeyboardBuilder()
            button = KeyboardButton
        else:
            keyboard = InlineKeyboardBuilder()
            button = InlineKeyboardButton

        for text, callback_data in buttons.items():
            if callback_data[0] == "url":
                buttons_list.append(button(text=text, url=callback_data[1]))

            else:
                buttons_list.append(button(text=text, callback_data=callback_data))

            if len(buttons_list) == interval:
                keyboard.row(*buttons_list)
                buttons_list.clear()

                interval_count += 1
                if interval_count == count:
                    interval = 1

        return keyboard.as_markup() if not is_builder else keyboard