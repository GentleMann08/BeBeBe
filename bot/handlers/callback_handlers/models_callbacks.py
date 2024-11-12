from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from ..states import LLM_Generation

models_router = Router()

@models_router.callback_query(F.data.endswith('_model'))
async def models_state(callback_query: CallbackQuery, state: FSMContext):
    model = callback_query.data.replace('_model', '')

    await state.set_state(LLM_Generation.text_to_model)
    await state.update_data(model=model)
    
    await state.update_data(model=model)
    