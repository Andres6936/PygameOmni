from enum import Enum, unique, auto


@unique
class NextScene(Enum):
    NONE = auto()
    EXIT = auto()
    MENU = auto()
    IN_GAME = auto()
