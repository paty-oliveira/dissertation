from framework.domain.IPipeline import IPipeline
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ImportFile import ImportFile
from framework.domain.Taxonomy import Taxonomy


class IdentificationSpeciePipeline(IPipeline):

    """
        Pipeline for the identification of species present in the dataset.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_IDENTIFICATION]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()
        self.__pipeline_steps = self.__add_pipeline_steps()

    def run(self):
        "Executes all the steps of the pipeline"

        for step in self.__pipeline_steps:
            result = step.execute()

            if result:
                return result

    def __add_pipeline_steps(self):
        "Adds the pipeline steps"

        steps = []

        steps.append(ImportFile(self.__filepath, self.__data_folder))
        steps.append(Taxonomy(self.__configuration, self.__filepath))

        return steps
