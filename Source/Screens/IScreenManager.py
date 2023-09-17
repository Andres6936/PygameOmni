from abc import ABC, abstractmethod


class IScreenManager(ABC):
    @abstractmethod
    def Surface(self):
        pass

    @abstractmethod
    def ScreenWidth(self):
        pass

    @abstractmethod
    def ScreenHeight(self):
        pass
