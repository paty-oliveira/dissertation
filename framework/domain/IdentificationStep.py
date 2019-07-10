from framework.domain.IStep import IStep
from framework.common.aux_functions import convert_path
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ImportSequencingFile import ImportSequecingFile
from framework.domain.PIPITSSequencePreparation import PIPITSSequencePreparation
from framework.domain.PIPITSitsExtraction import PIPITSitsExtraction
from framework.domain.PIPITSTaxonomicIdentification import PIPITSTaxonomicIdentification
from framework.domain.ReportWriter import ReportWriter
import pandas as pd
import os


class IdentificationStep(IStep):

    """
        Logic of the identification step.

        The steps from PIPITS are added. The command of each step
        are executed.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__params = params
        self.__execution = params[ParameterKeys.IDENTIFICATION_KEY]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()
        self.__pipits_steps = self.__add_pipits_steps()
        self.__phylotype_file = self.__configuration.get_phylotype_table_results()

    def execute(self):
        "Executes all steps from PIPITS"

        if self.__execution:
            filepath = self.__params[ParameterKeys.FILEPATH_IDENTIFICATION]
            importing_file = ImportSequecingFile(filepath, self.__data_folder).execute()

            for step in self.__pipits_steps:
                result = step.run_commands()

                if result:
                    specie = self.__get_specie_identification()
                    specie_identification_results = ReportWriter(
                        filepath
                    ).write_identification(specie)

                    return specie_identification_results

        else:
            pass

    def __add_pipits_steps(self):
        "Adds steps from PIPITS to execute later."

        steps = []

        steps.append(PIPITSSequencePreparation(self.__configuration))

        steps.append(PIPITSitsExtraction(self.__configuration))

        steps.append(PIPITSTaxonomicIdentification(self.__configuration))

        return steps

    def __get_specie_identification(self):
        "Obtains the specie identification from PIPITS process"

        phylotype_file = pd.read_csv(
            self.__phylotype_file, sep="\t", engine="python", encoding="utf-8"
        )
        pd.set_option("display.max_colwidth", 2000)
        fungi_taxonomy = phylotype_file["taxonomy"]

        return fungi_taxonomy
