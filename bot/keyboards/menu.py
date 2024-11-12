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
    
    @staticmethod
    async def to_start():
        buttons_dict = {
            "Menu": "to_start"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard
    
    @staticmethod
    async def models():
        models = {
            "gpt-neo-125M": "EleutherAI/gpt-neo-125M_model",
            "distilgpt2": "distilgpt2_model",
            "gpt2": "gpt2_model",
            "gpt2-medium": "gpt2-medium_model"
        }
        buttons_dict = models | {"Menu": "to_start"}
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard