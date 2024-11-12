from .callback_handlers import callbacks_routers
from .commands_handlers import command_routers
from .text_handlers import text_routers

routers_list = list()

routers_list.extend(callbacks_routers)
routers_list.extend(command_routers)
routers_list.extend(text_routers)