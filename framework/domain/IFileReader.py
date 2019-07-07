from abc import ABC, abstractmethod

class IFileReader(ABC):

    @abstractmethod
    def read(self, file):
        pass