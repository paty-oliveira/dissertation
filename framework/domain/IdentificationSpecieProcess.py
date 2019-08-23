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
        self.__filepath = params[ParameterKeys.FILEPATH_IDENTIFICATION]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()
        self.__steps = self.__add_step()

    def run(self):
        "Executes all the steps of the process."

        for step in self.__steps:
            identification = step.execute()

            if identification:
                return ExecutionCode.ID_SUCCESS

            return ExecutionCode.ID_FAILED

    def __add_step(self):
        "Adds the steps of the process."

        steps = []
        steps.append(FileImported(self.__filepath, self.__data_folder))
        steps.append(Taxonomy(self.__configuration, self.__filepath))

        return steps
