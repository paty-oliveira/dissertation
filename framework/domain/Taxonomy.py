from framework.domain.IStep import IStep
from framework.exceptions.exceptions import PipitsExecutionError
from abc import ABC, abstractmethod
import subprocess
import shutil
import pandas as pd


class IIdentification(ABC):

    """
        Interface that implements the specie identification behavior.
    """

    @abstractmethod
    def identify(self):
        pass


class Taxonomy(IStep):

    """
        It allows the identification of species present in the dataset.
    """

    def __init__(self, configuration, filepath):
        self.__configuration = configuration
        self.__filepath = filepath
        self.__list_identifiers = self.__add_identifiers()

    def execute(self):
        "Executes the identification pipeline, according the list of identifiers."

        for identifier in self.__list_identifiers:
            result = identifier.identify()

            if result:
                return result

    def __add_identifiers(self):
        "Adds the identifiers."

        list_identifiers = []
        list_identifiers.append(PipitsPipeline(self.__configuration, self.__filepath))

        return list_identifiers


class PipitsPipeline(IIdentification):

    """
        Pipeline for specie identification (PIPITS) from Bioconda library.
    """

    CMD_ARGS_READPAIRLIST = [
        "pispino_createreadpairslist",
        "-i",
        "rawdata",
        "-o",
        "readpairslist.txt",
    ]

    CMD_ARGS_SEQUENCEPREP = [
        "pispino_seqprep",
        "-i",
        "rawdata",
        "-o",
        "out_seqprep",
        "-l",
        "readpairslist.txt",
    ]

    CMD_ARGS_ITS_EXTRACTION = [
        "pipits_funits",
        "-i",
        "out_seqprep/prepped.fasta",
        "-o",
        "out_funits",
        "-x",
        "ITS2",
        "-v",
        "-r",
    ]

    CMD_ARGS_TAXONOMIC_ID = [
        "pipits_process",
        "-i",
        "out_funits/ITS.fasta",
        "-o",
        "out_process",
        "-v",
        "-r",
    ]

    def __init__(self, configuration, filepath):
        self.__tmp_identification = configuration.get_path_identification_process()
        self.__phylotype_file = configuration.get_phylotype_table_results()
        self.__folder_results = filepath

    def identify(self):
        "Execute all commands for identification of specie."

        try:
            pair_list = self.__generate_read_pairs_list()
            preprocessing = self.__preprocessing_sequence()
            extraction = self.__extract_its_regions()
            taxonomy = self.__analyze_taxonomy()
            result = self.__fungi_specie()

            if not result:
                raise PipitsExecutionError

        except PipitsExecutionError as error:
            print(error.message)

    def __analyze_taxonomy(self):
        """Return the identification of the fungal specie present in the sequencing files,
         throught the subprocess of PIPITS."""

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_TAXONOMIC_ID, cwd=self.__tmp_identification
        )

        if self.__is_success(process_to_execute):
            return True

    def __extract_its_regions(self):
        "Extract all ITS regions throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_ITS_EXTRACTION, cwd=self.__tmp_identification
        )

        if self.__is_success(process_to_execute):
            return True

    def __generate_read_pairs_list(self):
        "Create read pair list file throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_READPAIRLIST, cwd=self.__tmp_identification
        )

        if self.__is_success(process_to_execute):
            return True

    def __fungi_specie(self):
        "Obtains the specie identification from PipitsPipeline process"

        phylotype_results = shutil.copy(self.__phylotype_file, self.__folder_results)

        return phylotype_results

    def __is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0

    def __preprocessing_sequence(self):
        "Preprocess the sequencing files throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_SEQUENCEPREP, cwd=self.__tmp_identification
        )

        if self.__is_success(process_to_execute):
            return True
