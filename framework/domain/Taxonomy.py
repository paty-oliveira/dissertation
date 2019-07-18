from framework.domain.IStep import IStep
from abc import ABC, abstractmethod
import subprocess
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
        Allows the identification of species present in the dataset.
    """

    def __init__(self, configuration):
        self.__configuration = configuration
        self.__list_identifiers = self.__add_identifiers()

    def execute(self):
        for identifier in self.__list_identifiers:
            result = identifier.identify()

            if result:
                return result

    def __add_identifiers(self):
        list_identifiers = []
        list_identifiers.append(Pipits(self.__configuration))

        return list_identifiers


class Pipits(IIdentification):

    """
        Run the Bioconda library PIPITS for specie identification.
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

    def __init__(self, configuration):
        self.__configuration = configuration
        self.__tmp_identification = (
            self.__configuration.get_path_identification_process()
        )
        self.__phylotype_file = self.__configuration.get_phylotype_table_results()

    def is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0

    def identify(self):
        "Execute all commands for identification of specie."

        self.__generate_read_pairs_list()
        self.__preprocessing_sequence()
        self.__extract_its_regions()
        self.__analyze_taxonomy()
        result = self.__get_specie_identification()

        return result

    def __generate_read_pairs_list(self):
        "Create read pair list file throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            Pipits.CMD_ARGS_READPAIRLIST, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True

    def __preprocessing_sequence(self):
        "Preprocess the sequencing files throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            Pipits.CMD_ARGS_SEQUENCEPREP, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True

    def __extract_its_regions(self):
        "Extract all ITS regions throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            Pipits.CMD_ARGS_ITS_EXTRACTION, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True

    def __analyze_taxonomy(self):
        """Return the identification of the fungal specie present in the sequencing files,
         throught the subprocess of PIPITS."""

        process_to_execute = subprocess.call(
            Pipits.CMD_ARGS_TAXONOMIC_ID, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True

    def __get_specie_identification(self):
        "Obtains the specie identification from PIPITS process"

        phylotype_file = pd.read_csv(
            self.__phylotype_file, sep="\t", engine="python", encoding="utf-8"
        )
        pd.set_option("display.max_colwidth", 2000)
        fungi_taxonomy = phylotype_file["taxonomy"]

        return fungi_taxonomy
