from framework.domain.pipeline import Pipeline
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.ImportSequencingFile import ImportSequecingFile
from framework.domain.PipitsProcess import PipitsProcess
from framework.domain.ReportWriter import ReportWriter
import pandas as pd
import os


class IdentificationSpeciePipeline(Pipeline):

    """
        Logic of the identification step.

        The steps from PIPITS are added. The command of each step
        are executed.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_IDENTIFICATION]
        self.__data_folder = self.__configuration.get_path_data_folder_identification()
        self.__pipeline_steps = self.__add_pipeline_steps()

    def execute(self):
        "Executes all steps from PIPITS"

        for step in self.__pipeline_steps:
            result = step.execute()

            if result:
                identification_results = ReportWriter(self.__filepath).write_identification(result)

                return identification_results

        # if self.__execution:
        #     filepath = self.__params[ParameterKeys.FILEPATH_IDENTIFICATION]
        #     importing_file = ImportSequecingFile(filepath, self.__data_folder).execute()

        #     for step in self.__pipits_steps:
        #         result = step.run_commands()

        #         if result:
        #             specie = self.__get_specie_identification()
        #             specie_identification_results = ReportWriter(
        #                 filepath
        #             ).write_identification(specie)

        #             return specie_identification_results

        # else:
        #     pass

    def __add_pipeline_steps(self):
        "Adds steps from PIPITS to execute later."

        steps = []

        steps.append(ImportSequecingFile(self.__filepath, self.__data_folder))
        steps.append(PipitsProcess(self.__configuration))
        
        return steps

