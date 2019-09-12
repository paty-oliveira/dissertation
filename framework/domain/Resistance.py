from framework.domain.IStep import IStep
from framework.domain.IPipeline import IPipeline
from framework.domain.FileReading import FileReading
from framework.domain.InformationExtraction import InformationExtraction
from framework.domain.SequenceTrimmed import SequenceTrimmed
from framework.domain.SequenceWithoutPrimer import SequenceWithoutPrimer
from framework.domain.Translation import Translation
from framework.domain.Mutation import Mutation
from framework.domain.AntifungalResistance import AntifungalResistance
from framework.common.ParameterKeys import ExecutionCode
import os


class Resistance(IStep):

    """
        It allows the integration of pipelines to detect the antifungal
        resistance.
    """

    def __init__(self, configuration, filepath, specie, gene, primers):
        self.__configuration = configuration
        self.__filepath = filepath
        self.__specie = specie
        self.__gene = gene
        self.__primers = primers
        self.__pipelines = self.__add_pipeline()

    def execute(self):
        "Executes the pipeline, according to the list of pipelines available."

        for pipeline in self.__pipelines:
            result = pipeline.run()

            if result:
                return ExecutionCode.ANTI_SUCCESS

            else:
                return ExecutionCode.ANTI_FAILED

    def __add_pipeline(self):
        "Adds pipelines."

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


class AntifungalResistancePipeline(IPipeline):

    """
        Example of pipeline for the detection of the antifungal
        resistance present in the file inserted. 
    """

    def __init__(self, configuration, filepath, specie, gene, primers):
        self.__ref_genes_filepath = configuration.get_antifungal_genes_file()
        self.__mardy_file = configuration.get_mardy_file()
        self.__input_file = filepath
        self.__specie = specie
        self.__gene = gene
        self.__primers = primers
        self.__alphabet = "AGTC"

    def run(self):
        "Executes all the steps of the pipeline."

        stage_1 = self.__read()
        stage_2 = self.__extract()
        stage_3 = self.__remove_primer(stage_1)
        stage_4 = self.__trims(stage_3, stage_2[0])
        stage_5 = self.__translate(stage_3, stage_4)
        stage_6 = self.__mutation(stage_5[1], stage_5[0], stage_2[1])
        stage_7 = self.__antifungals(stage_2[2], stage_6)
        output_file = self.__write(stage_6, stage_7)

        if output_file:
            return True

        return False

    def __antifungals(self, reference_data, mutations):
        """
            Creates the AntifungalResistance object to identify
            the antifungals to which the organism is resistant.
        """

        antifungals = AntifungalResistance(reference_data, mutations).execute()

        return antifungals

    def __extract(self):
        "Creates the Extract object to extract information."

        reference_sequence, position, mardy_information = InformationExtraction(
            self.__ref_genes_filepath, self.__mardy_file, self.__specie, self.__gene
        ).execute()

        return reference_sequence, position, mardy_information

    def __mutation(self, aminoacid_ref, aminoacid_query, position):
        "Creates the Mutation object to identifies the amino acid substitutions "

        mutations = Mutation(aminoacid_ref, aminoacid_query, position).execute()

        return mutations

    def __read(self):
        "Creates the Read object to read the file."

        dna_sequences = FileReading(self.__input_file).execute()
        if dna_sequences:
            return dna_sequences[1]

    def __remove_primer(self, query_sequence):
        "Creates the Remove object to remove primers and trims sequences."

        new_sequence = SequenceWithoutPrimer(
            query_sequence, self.__primers, self.__alphabet
        ).execute()

        return new_sequence

    def __translate(self, sequence_1, sequence_2):
        "Creates the Translation object to translate the dna sequences."

        sequences = [sequence_1, sequence_2]
        aminoacid_sequence = Translation(sequences).execute()

        return aminoacid_sequence

    def __trims(self, query_sequence, ref_sequence, limit_number=11):

        new_sequence = SequenceTrimmed(
            query_sequence, ref_sequence, limit_number
        ).execute()

        return new_sequence

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

            if antifungals:
                for result in antifungals:
                    output_file.write(result + "\n")
            else:
                output_file.write("No antifungal resistance detected.")

        return output_file
