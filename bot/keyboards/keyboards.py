from dataclasses import dataclass
from .menu import Menu

@dataclass
class Keyboard:

    @property
    def menu(self) -> Menu:
        return Menu()