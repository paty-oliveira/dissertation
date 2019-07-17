from framework.domain.PipelineStep import PipelineStep
import subprocess
import pandas as pd 


class PipitsProcess(PipelineStep):

    """
        Represent the PIPITS_PREP step from PIPITS.
        
        And execute the commands of this step.

    """

    cmd_args_readpairlist = [
        "pispino_createreadpairslist",
        "-i",
        "rawdata",
        "-o",
        "readpairslist.txt",
    ]

    cmd_args_sequenceprep = [
        "pispino_seqprep",
        "-i",
        "rawdata",
        "-o",
        "out_seqprep",
        "-l",
        "readpairslist.txt",
    ]
    
    cmd_args_its_extraction = [
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
    
    cmd_args_taxonomic_id = [
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
        self.__tmp_identification = self.__configuration.get_path_identification_process()
        self.__phylotype_file = self.__configuration.get_phylotype_table_results()


    def is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0


    def execute(self):
        "Execute all commands of each subprocess called."

        try:
            self.__generate_read_pairs_list()
            self.__preprocessing_sequence()
            self.__extract_its_regions()
            self.__analyze_taxonomy()
            self.__get_specie_identification()

        else:
            pass


    def __generate_read_pairs_list(self):
        "Create read pair list file throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            PipitsProcess.cmd_args_readpairlist, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True


    def __preprocessing_sequence(self):
        "Preprocess the sequencing files throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            PipitsProcess.cmd_args_sequenceprep, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True

    
    def __extract_its_regions(self):
        "Extract all ITS regions throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            PipitsProcess.cmd_args_its_extraction, cwd=self.__tmp_identification
        )

        if self.is_success(process_to_execute):
            return True


    def __analyze_taxonomy(self):
        """Return the identification of the fungal specie present in the sequencing files,
         throught the subprocess of PIPITS."""

        process_to_execute = subprocess.call(
            PipitsProcess.cmd_args_taxonomic_id, cwd=self.__tmp_identification
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
