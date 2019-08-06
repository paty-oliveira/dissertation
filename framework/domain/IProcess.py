from abc import ABC, abstractmethod


class IProcess(ABC):

    """
       Interface that implements the pipeline behavior. 
    """

    @abstractmethod
    def run(self):
        pass
