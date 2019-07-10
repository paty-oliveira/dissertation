from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def show(self):
        pass
