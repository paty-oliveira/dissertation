from framework.domain.IStep import IStep
from framework.domain.Import import Import
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.Read import Read
from framework.domain.Extract import Extract
from framework.domain.Remove import Remove
from framework.domain.Translation import Translation
from framework.domain.Mutation import Mutation
from framework.domain.AntifungalResistance import AntifungalResistance
import os
import urllib.request
from abc import ABC, abstractmethod


class IPipeline(ABC):

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
        self.__input_file = filepath
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
                self.__input_file,
                self.__specie,
                self.__gene,
                self.__primers,
            )
        )
        return pipelines


class AntifungalResistancePipeline(IPipeline):

    """
        Example of pipeline for the detection of the antifungal resistance present in the file imported. 
    """

    def __init__(self, configuration, filepath, specie, gene, primers):
        self.__ref_genes_filepath = configuration.get_antifungal_genes_file()
        self.__mardy_file = configuration.get_mardy_file()
        self.__detection_resistance_folder = (
            configuration.get_path_detection_resistance_process()
        )
        self.__input_file = filepath
        self.__specie = specie
        self.__gene = gene
        self.__primer = primers
        self.__dowmload(self.__detection_resistance_folder)

    def run(self):
        "Executes all the steps of the pipeline."

        stage_1 = self.__read()
        stage_2 = self.__extract()
        stage_3 = self.__remove(stage_1, stage_2[0])
        stage_4 = self.__translate(stage_3)
        stage_5 = self.__mutation(stage_4[1], stage_4[0], stage_2[1])
        stage_6 = self.__antifungals(stage_2[2], stage_5)
        output_file = self.__write(stage_5, stage_6)

    def __antifungals(self, reference_data, mutations):
        "Creates the AntifungalResistance object to identify the antifungals to which the organism is resistant."

        antifungals = AntifungalResistance(reference_data, mutations).execute()

        return antifungals

    def __extract(self):
        "Creates the Extract object to extract information."

        reference_sequence, position, mardy_information = Extract(
            self.__ref_genes_filepath, self.__mardy_file, self.__specie, self.__gene
        ).execute()

        return reference_sequence, position, mardy_information

    def __dowmload(self, path):
        "Executes the download of the file from Mardy database."

        url = " http://mardy.dide.ic.ac.uk/session_files/DB_by_drug.csv"
        file_name = os.path.join(path, "DB_by_drug.csv")
        urllib.request.urlretrieve(url, file_name)

    def __mutation(self, aminoacid_ref, aminoacid_query, position):
        "Creates the Mutation object to identifies the amino acid substitutions "

        mutations = Mutation(aminoacid_ref, aminoacid_query, position).execute()

        return mutations

    def __read(self):
        "Creates the Read object to read the file."

        dna_sequences = Read(self.__input_file).execute()
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

    def __write(self, mutations, antifungals):
        "Writes the results of the detection of resistance on the csv file."

        output_folder = os.path.dirname(self.__input_file)

        with open(
            os.path.join(output_folder, "antifungal_detection_results.csv"), "w"
        ) as output_file:

            header = "Reference Position Substitutions\n"
            mutations_results = "\n".join(
                "{}".format(mutation) for mutation in mutations
            )
            output_file.write(header)
            output_file.write(mutations_results)
            output_file.write("\n")
            output_file.write("\nAntifungal Resistance \n")

            for result in antifungals:
                output_file.write(result + "\n")

        return output_file
