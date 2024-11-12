from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from ..states import LLM_Generation

llm_generation_router = Router()

@llm_generation_router.message(StateFilter(LLM_Generation.text_to_model), F.text != '/exit')
async def llm_generation(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    model = data.get("model")

    await message.answer(f'*answer by "{model}" model*')