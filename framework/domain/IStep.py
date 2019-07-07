from abc import ABC, abstractmethod


class IStep(ABC):

    @abstractmethod
    def execute(self):
        pass


        