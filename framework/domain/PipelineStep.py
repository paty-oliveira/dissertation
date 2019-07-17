from abc import ABC, abstractmethod

class PipelineStep(ABC):

    @abstractmethod
    def execute(self):
        pass