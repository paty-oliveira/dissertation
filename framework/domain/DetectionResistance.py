from framework.domain.IStep import IStep
from framework.domain.Import import Import
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.Read import Read
from framework.domain.Extract import Extract
from framework.domain.Remove import Remove
from framework.domain.Translation import Translation
from framework.domain.Mutation import Mutation
import os
from abc import ABC, abstractmethod


class IResistance(ABC):

    """
        Interface that implements the antifungal resistance behavior.
    """

    @abstractmethod
    def run(self):
        pass


class DetectionResistance(IStep):

    """
        It allows the detection of resistance present in the file imported.
    """

    def __init__(self, configuration, filepath, specie, gene, primers):
        self.__configuration = configuration
        self.__filepath = filepath
        self.__specie = specie
        self.__gene = gene
        self.__primers = primers
        self.__pipelines = self.__add_pipeline()

    def execute(self):
        "Execute the detection resistance pipeline, accordinf the list of pipelines."

        for pipeline in self.__pipelines:
            result = pipeline.run()

            if result:
                return result

    def __add_pipeline(self):
        "Add the pipelines."

        pipelines = []

        pipelines.append(
            AntifungalResistancePipeline(
                self.__configuration,
                self.__filepath,
                self.__specie,
                self.__gene,
                self.__primers,
            )
        )
        return pipelines


class AntifungalResistancePipeline(IResistance):

    """
        Example of pipeline for the detection of the antifungal resistance present in the file imported. 
    """

    def __init__(self, configuration, filepath, specie, gene, primers):
        self.__configuration = configuration
        self.__filepath = filepath
        self.__specie = specie
        self.__gene = gene
        self.__primer = primers

    def run(self):
        "Executes all the steps of the pipeline."

        stage_1 = self.__read()
        stage_2 = self.__extract()
        stage_3 = self.__remove(stage_1, stage_2[0])
        stage_4 = self.__translate(stage_3)
        stage_5 = self.__mutation(stage_4[1], stage_4[0], stage_2[1])
        output_file = self.__write(stage_5)

    def __extract(self):
        "Creates the Extract object to extract information."

        reference_sequence, position = Extract(
            self.__configuration, self.__specie, self.__gene
        ).execute()

        return reference_sequence, position

    def __mutation(self, aminoacid_ref, aminoacid_query, position):
        "Creates the Mutation object to identifies the amino acid substitutions "

        mutations = Mutation(aminoacid_ref, aminoacid_query, position).execute()

        return mutations

    def __read(self):
        "Creates the Read object to read the file."

        dna_sequences = Read(self.__filepath).execute()
        if dna_sequences:
            return dna_sequences[1]

    def __remove(self, query_sequence, ref_sequence):
        "Creates the Remove object to remove primers and trims sequences."

        query_trimmed, ref_trimmed = Remove(
            query_sequence, ref_sequence, self.__primer
        ).execute()

        return query_trimmed, ref_trimmed

    def __translate(self, sequence):
        "Creates the Translation object to translate the dna sequences."

        aminoacid_sequence = Translation(sequence).execute()

        return aminoacid_sequence

    def __write(self, results):
        "Writes the results of amino acid substitutions on the csv file."

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
