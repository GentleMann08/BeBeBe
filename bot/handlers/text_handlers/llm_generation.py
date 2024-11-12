from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

llm_generation_router = Router()

@llm_generation_router.message(StateFilter("llm_generation"))
async def llm_generation(message: Message, bot: Bot, state: FSMContext):
    message.answer('[text]')