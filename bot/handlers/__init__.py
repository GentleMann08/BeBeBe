from .callback_handlers import callbacks_routers
from .commands_handlers import command_routers

routers_list = list()

routers_list.extend(callbacks_routers)
routers_list.extend(command_routers)