from aiogram.fsm.state import State, StatesGroup

class LLM_Generation(StatesGroup):
    text_to_model = State()