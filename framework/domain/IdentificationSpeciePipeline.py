from framework.domain.IPipeline import IPipeline
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ImportFile import ImportFile
from framework.domain.PipitsProcess import PipitsProcess
from framework.domain.WriteResult import WriteResult


class IdentificationSpeciePipeline(IPipeline):

    """
        Pipeline for the identification of species present in the dataset.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_IDENTIFICATION]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()
        self.__pipeline_steps = self.__add_pipeline_steps()

    def execute(self):
        "Executes all steps of the pipeline"

        for step in self.__pipeline_steps:
            result = step.execute()

            if result:
                identification_results = WriteResult(self.__filepath).write_identification(result)

                return identification_results


    def __add_pipeline_steps(self):
        "Adds the pipeline steps"

        steps = []

        steps.append(ImportFile(self.__filepath, self.__data_folder))
        steps.append(PipitsProcess(self.__configuration))
        
        return steps

