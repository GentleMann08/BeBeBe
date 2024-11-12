from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from ..states import LLM_Generation
from ai.scripts.LLM import LLM_bot

llm_generation_router = Router()

@llm_generation_router.message(StateFilter(LLM_Generation.text_to_model), F.text != '/exit')
async def llm_generation(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    LLM_model = data.get("LLM_model")
    
    if not LLM_model:
        await message.answer("Error: Model could not be loaded.")
        return

    response = await LLM_model.generate_text(prompt=message.text, max_len=120)
    await message.answer(response)