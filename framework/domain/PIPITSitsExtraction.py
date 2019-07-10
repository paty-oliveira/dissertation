from .IIdentificationProcess import IIdentificationProcess
import subprocess


class PIPITSitsExtraction(IIdentificationProcess):

    """
        Represent the PIPITS_FUNITS step from PIPITS.

        And execute the commands of this step.

    """

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

    def __init__(self, configuration):
        self.__config = configuration
        self.__root_folder = self.__config.get_path_identification_process()

    def is_success(self, process):
        "Verify if the subprocess called happened."

        return process == 0

    def run_commands(self):
        "Execute all commands of each subprocess called."

        if True:
            self.__extract_its()

        else:
            pass

    def __extract_its(self):
        "Extract all ITS regions throught the subprocess of PIPITS."

        process_to_execute = subprocess.call(
            PIPITSitsExtraction.cmd_args_its_extraction, cwd=self.__root_folder
        )

        if self.is_success(process_to_execute):
            return True
