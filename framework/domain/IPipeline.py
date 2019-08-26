from abc import ABC, abstractmethod


class IPipeline(ABC):

    """
        Interface that implements the antifungal resistance behavior.
    """

    @abstractmethod
    def run(self):
        pass
