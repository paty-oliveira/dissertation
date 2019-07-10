from .IIdentificationProcess import IIdentificationProcess
import subprocess


class PIPITSTaxonomicIdentification(IIdentificationProcess):

    """
        Represent the PIPITS_PROCESS step from PIPITS.

        And execute the commands of this step.

    """

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
        self.__root_folder = self.__configuration.get_path_identification_process()

    def is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0

    def run_commands(self):
        "Execute all commands of each subprocess called."

        if True:
            self.__get_taxonomic_id()

        else:
            pass

    def __get_taxonomic_id(self):
        """Return the identification of the fungal specie present in the sequencing files,
         throught the subprocess of PIPITS."""

        process_to_execute = subprocess.call(
            PIPITSTaxonomicIdentification.cmd_args_taxonomic_id, cwd=self.__root_folder
        )

        if self.is_success(process_to_execute):
            return True
