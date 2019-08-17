from framework.common.ParameterKeys import ParameterKeys
from framework.application.BuildDataFlow import BuildDataFlow
from framework.presentation.IUserInterface import IUserInterface
from framework.exceptions.exceptions import (
    WrongGeneError,
    WrongPrimerError,
    WrongSpecieError,
    WrongFilePath,
)
import sys
import subprocess
import os


def convert_path(path):
    "Convert windows path format for linux format."

    cmd_args = ["wslpath", path]
    result = (
        subprocess.run(cmd_args, stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .replace("\n", "")
    )
    return str(result)


class ConsoleView(IUserInterface):
    """
        Console View presents the user with the form for running the pipeline
    """

    def __init__(self, controller):
        self.__controller = controller

    def show(self):
        "Presents the user with the form needed for running the pipeline."

        self.__headline()

        while True:
            params, should_exit = self.__user_options()
            print("\nRunning pipeline...")

            results = self.__controller.execute(params)
            print(results)

            if should_exit:
                break

    def __headline(self):
        "Prints the headline of the framework."

        print("##################################################")
        print("#### Identification and Detection - Framework ####")
        print("##################################################")

    def __is_gene(self, gene):
        "Checks if is the correct gene."

        return gene in ["ERG11", "FKS1", "FKS2"]

    def __is_primer(self, primer):
        "Checks if primer has the correct characters."

        return set(primer).issubset("AGTC")

    def __is__specie(self, specie):
        "Checks if is the correct specie."

        return specie in [
            "Candida albicans",
            "Candida glabrata",
            "Candida tropicalis",
            "Candida parapsilosis",
        ]

    def __is_path(self, path):
        "Checks if the path is valid."

        return os.path.exists(path)

    def __mock_options(self):
        "Represents a dictionary with parameters for test mode."

        params = {
            ParameterKeys.IDENTIFICATION_KEY: False,
            ParameterKeys.MUTATION_KEY: True,
            ParameterKeys.FILEPATH_DETECTION: convert_path(
                "C:/Users/anapatricia/Documents/test_data/test_calbicans_erg11.txt"
            ),
            ParameterKeys.SPECIE_NAME: "Candida albicans",
            ParameterKeys.GENE_NAME: "ERG11",
            ParameterKeys.FORWARD_PRIMER: "AAAAAT",
            ParameterKeys.REVERSE_PRIMER: "TTTTTA",
        }
        should_exit = True
        return params, should_exit

    def __parse_response(self, response, default="y"):
        "Parses the response given by the user."

        return (
            response == default.lower() or response == default.upper() or response == ""
        )

    def __user_options(self):
        "The user responds to the form and gets the parameters."

        should_exit = False
        params = {}

        response = input("Test mode [y|N]: ")
        if self.__parse_response(response):
            params, should_exit = self.__mock_options()

            return params, should_exit

        else:
            while True:
                response = input("Identify specie [Y|n]:")
                params[ParameterKeys.IDENTIFICATION_KEY] = self.__parse_response(
                    response
                )
                if self.__parse_response(response):
                    filepath_identification = input("File directory: ")
                    if self.__is_path(filepath_identification):
                        params[ParameterKeys.FILEPATH_IDENTIFICATION] = convert_path(
                            filepath_identification
                        )
                    else:
                        raise WrongFilePath
                        break

                response = input("Detect mutations? [Y|n]: ")
                params[ParameterKeys.MUTATION_KEY] = self.__parse_response(response)
                if self.__parse_response(response):
                    filepath_detection = input("File directory: ")
                    if self.__is_path(filepath_detection):
                        params[ParameterKeys.FILEPATH_DETECTION] = convert_path(
                            filepath_detection
                        )
                    else:
                        raise WrongFilePath
                        break

                    specie_name = input("Specie name: ").capitalize()
                    if self.__is__specie(specie_name):
                        params[ParameterKeys.SPECIE_NAME] = specie_name
                    else:
                        raise WrongSpecieError
                        break

                    gene_name = input("Gene: ").upper()
                    if self.__is_gene(gene_name):
                        params[ParameterKeys.GENE_NAME] = gene_name
                    else:
                        raise WrongGeneError
                        break

                    forward_primer = input("Forward primer: ").upper()
                    if self.__is_primer(forward_primer):
                        params[ParameterKeys.FORWARD_PRIMER] = forward_primer
                    else:
                        raise WrongPrimerError
                        break

                    reverse_primer = input("Reverse primer: ").upper()
                    if self.__is_primer(reverse_primer):
                        params[ParameterKeys.REVERSE_PRIMER] = reverse_primer
                    else:
                        raise WrongPrimerError
                        break

                response = input("Will you continue executing other pipelines? [y|N]: ")
                should_exit = self.__parse_response(response, default="n")

                return params, should_exit
