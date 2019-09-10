from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def display(self):
        pass
