from framework.domain.IPipeline import IPipeline
from framework.domain.ImportFile import ImportFile
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ReadFile import ReadFile
from framework.domain.ExtractInformation import ExtractInformation
from framework.domain.WriteResult import WriteResult
from framework.domain.Mutation import Mutation


class DetectionMutationPipeline(IPipeline):

    """
        Pipeline for the detection of the mutations presente in the dataset.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_DETECTION]
        self.__specie = params[ParameterKeys.SPECIE_NAME]
        self.__gene = params[ParameterKeys.GENE_NAME]
        self.__data_folder = self.__configuration.get_path_data_folder_mutation()
        self.__list_steps = self.__add_steps()

    def execute(self):
        "Executes all the steps of the pipeline."

        for step in self.__list_steps:
            result = step.execute()

            if result:
                mutations_results = WriteResult(self.__filepath).write_mutations(result)

                return mutations_results

    def __add_steps(self):
        "Adds the pipeline steps."

        # Falta adicionar os restantes steps da identificação das mutações e associação à resistencia aos antifungicos
        list_steps = []
        list_steps.append(ImportFile(self.__filepath, self.__data_folder))
        list_steps.append(ReadFile(self.__data_folder))
        list_steps.append(ExtractInformation(self.__configuration, self.__specie, self.__gene))

        return list_steps
