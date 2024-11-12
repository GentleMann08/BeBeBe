from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu import Menu

llm_commands_router = Router()

@llm_commands_router.message(Command('exit'))
async def start_handler(message: Message, bot: Bot, state: FSMContext):


    keyboard = await Menu.models()
    last_messafe = await message.answer(
        text="Select your AI-Model",
        reply_markup=keyboard
        )
    
    await state.clear()
    await state.update_data(last_message_id=last_messafe.message_id)