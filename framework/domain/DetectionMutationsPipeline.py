from framework.domain.IPipeline import IPipeline
from framework.domain.Import import Import
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.Read import Read
from framework.domain.Extract import Extract
from framework.domain.Remove import Remove
from framework.domain.Translation import Translation
from framework.domain.Mutation import Mutation
import os


def put_element_into_list(string):
    return [element for element in string.split(" ")]


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

    def run(self):
        "Executes all the steps of the pipeline."

        stage_1 = self.__read()
        stage_2 = self.__extract()
        stage_3 = self.__remove(stage_1, stage_2[0])
        stage_4 = self.__translate(stage_3)
        stage_5 = self.__mutation(stage_4[1], stage_4[0], stage_2[1])
        output_file = self.__write(stage_5)

    def __extract(self):
        reference_sequence, position = Extract(
            self.__configuration, self.__specie, self.__gene
        ).execute()

        return reference_sequence, position

    def __mutation(self, aminoacid_ref, aminoacid_query, position):
        mutations = Mutation(aminoacid_ref, aminoacid_query, position).execute()

        return mutations

    def __read(self):
        dna_sequences = Read(self.__filepath).execute()
        if dna_sequences:
            return dna_sequences[1]

    def __remove(self, query_sequence, ref_sequence):
        query_trimmed, ref_trimmed = Remove(
            query_sequence, ref_sequence, self.__primer
        ).execute()

        return query_trimmed, ref_trimmed

    def __translate(self, sequence):
        aminoacid_sequence = Translation(sequence).execute()

        return aminoacid_sequence

    def __write(self, results):
        output_folder = os.path.dirname(self.__filepath)

        with open(
            os.path.join(output_folder, "mutations_result.csv"), "w"
        ) as output_file:
            header = "Reference, Position, Substitutions"
            to_write = "\n".join(
                "{}, {}, {}".format(str(x[0]), str(x[1]), str(x[2])) for x in results
            )
            output_file.write(header)
            output_file.write(to_write)

        return output_file
