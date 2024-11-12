from .start_handler import start_router
from .llm_handlers import llm_commands_router

command_routers = [
    start_router,
    llm_commands_router
]