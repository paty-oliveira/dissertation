from framework.domain.IPipeline import IPipeline
from framework.domain.ImportFile import ImportFile
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ReadFile import ReadFile
from framework.domain.ExtractInformation import ExtractInformation
from framework.domain.RemoveSequence import RemoveSequence
from framework.domain.Translation import Translation
from framework.domain.WriteResult import WriteResult
from framework.domain.Mutation import Mutation
from framework.common.Auxiliar import put_element_into_list


class DetectionMutationPipeline(IPipeline):

    """
        Pipeline for the detection of the mutations presente in the dataset.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_DETECTION]
        self.__specie = params[ParameterKeys.SPECIE_NAME]
        self.__gene = params[ParameterKeys.GENE_NAME]
        self.__primer = put_element_into_list(params[ParameterKeys.PRIMERS])
        self.__data_folder = self.__configuration.get_path_data_folder_mutation()
        self.__list_steps = self.__add_steps()

    def execute(self):
        "Executes all the steps of the pipeline."

        # Necessário reformular toda esta parte para construir a pipeline com
        # as classes criadas
        # ImportFile -> ReadFile -> ExtractInformation -> RemoveSequences -> Translation -> Mutations -> etc

        for step in self.__list_steps:
            sbjt_sequence = step.execute()

            if sbjt_sequence:
                ref_sequence, position = ExtractInformation(
                    self.__configuration, self.__specie, self.__gene
                ).execute()

                sbjct_trimmed, ref_trimmed = RemoveSequence(
                    sbjt_sequence, ref_sequence, self.__primer
                ).execute()

                sbjct_aminoacid_seq = Translation(sbjct_trimmed).execute()
                ref_aminoacif_seq = Translation(ref_trimmed).execute()

                mutations = Mutation(ref_aminoacif_seq, sbjct_aminoacid_seq).execute()

                if mutations:
                    result = WriteResult(self.__filepath).write(mutations)

                    return result

                return "No mutations identified."

            return False

        return False

    def __add_steps(self):
        "Adds the pipeline steps."

        # Falta adicionar os restantes steps da identificação das mutações e associação à resistencia aos antifungicos
        list_steps = []
        list_steps.append(ImportFile(self.__filepath, self.__data_folder))
        list_steps.append(ReadFile(self.__data_folder))

        return list_steps
