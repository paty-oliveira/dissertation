from abc import ABC, abstractmethod


class IIdentificationProcess(ABC):

    @abstractmethod
    def run_commands(self):
        pass

    @abstractmethod
    def is_success(self, process):
        pass


        