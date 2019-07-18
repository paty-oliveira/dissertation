from abc import ABC, abstractmethod


class IPipeline(ABC):

    """
       Interface that implements the pipeline behavior. 
    """


    @abstractmethod
    def execute(self):
        pass
