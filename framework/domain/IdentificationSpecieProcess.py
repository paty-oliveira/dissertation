from framework.domain.IProcess import IProcess
from framework.common.ParameterKeys import ParameterKeys, ExecutionCode
from framework.domain.FileImported import FileImported
from framework.domain.Taxonomy import Taxonomy


class IdentificationSpecieProcess(IProcess):

    """
        Logic of the identification specie process.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__params = params
        self.__filepath = ""
        self.__execution = params[ParameterKeys.IDENTIFICATION_KEY]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()

    def run(self):
        "Executes all the steps of the process."

        if self.__execution:
            self.__filepath = self.__params[ParameterKeys.FILEPATH_IDENTIFICATION]
            steps = self.__add_step()
            execution_code = [step.execute() for step in steps]

            return execution_code
            
        else:
            pass

    def __add_step(self):
        "Adds the steps of the process."

        steps = []
        steps.append(FileImported(self.__filepath, self.__data_folder))
        steps.append(Taxonomy(self.__configuration, self.__filepath))

        return steps
