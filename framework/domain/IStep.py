from abc import ABC, abstractmethod

class IStep(ABC):

    """
        Interface that implements the step behavior.
    """

    @abstractmethod
    def execute(self):
        pass