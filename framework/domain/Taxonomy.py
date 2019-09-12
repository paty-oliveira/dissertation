from framework.domain.IStep import IStep
from framework.domain.IPipeline import IPipeline
from framework.common.ParameterKeys import ExecutionCode
from framework.common.Utilities import exists_file
from abc import ABC, abstractmethod
import subprocess
import shutil
import pandas as pd


class Taxonomy(IStep):

    """
        It allows the integration of pipelines to identify the species.
    """

    def __init__(self, configuration, filepath):
        self.__configuration = configuration
        self.__results_folder = filepath
        self.__pipelines = self.__add_pipelines()

    def execute(self):
        "Executes the pipeline, according to the list of pipelines available."

        for pipeline in self.__pipelines:
            result = pipeline.run()

            if result:
                return ExecutionCode.ID_SUCCESS

            else:
                return ExecutionCode.ID_FAILED

    def __add_pipelines(self):
        "Adds pipelines."

        list_pipelines = []
        list_pipelines.append(
            PipitsPipeline(self.__configuration, self.__results_folder)
        )

        return list_pipelines


class PipitsPipeline(IPipeline):

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

    def __init__(self, configuration, results_folder):
        self.__folder_identification_process = (
            configuration.get_path_identification_process()
        )
        self.__phylotype_file = configuration.get_phylotype_table_results()
        self.__results_folder = results_folder

    def run(self):
        "Execute all commands for identification of specie."

        while True:
            self.__generate_read_pairs_list()
            self.__preprocessing_sequence()
            self.__extract_its_regions()
            self.__analyze_taxonomy()
            self.__fungi_specie()

            if exists_file(self.__phylotype_file):
                return True

            else:
                return False

    def __analyze_taxonomy(self):
        """Return the identification of the fungal specie present in the sequencing files,
         throught the subprocess of PIPITS."""

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_TAXONOMIC_ID,
            cwd=self.__folder_identification_process,
        )

        if self.__is_success(process_to_execute):
            return True

    def __extract_its_regions(self):
        "Extract all ITS regions throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_ITS_EXTRACTION,
            cwd=self.__folder_identification_process,
        )

        if self.__is_success(process_to_execute):
            return True

    def __generate_read_pairs_list(self):
        "Create read pair list file throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_READPAIRLIST,
            cwd=self.__folder_identification_process,
        )

        if self.__is_success(process_to_execute):
            return True

    def __fungi_specie(self):
        "Obtains the specie identification from PipitsPipeline process"

        phylotype_results = shutil.copy(self.__phylotype_file, self.__results_folder)

        return phylotype_results

    def __is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0

    def __preprocessing_sequence(self):
        "Preprocess the sequencing files throught the subprocess of PipitsPipeline."

        process_to_execute = subprocess.call(
            PipitsPipeline.CMD_ARGS_SEQUENCEPREP,
            cwd=self.__folder_identification_process,
        )

        if self.__is_success(process_to_execute):
            return True
