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


def valid_path(path):
    "Checks if the path is valid."

    return os.path.exists(path)


def valid_primer(primer):
    "Checks if primer has the correct characters."

    return set(primer).issubset("AGTC")


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
            self.__show_status(results)

            if should_exit:
                break

    def __headline(self):
        "Prints the headline of the framework."

        print("##################################################")
        print("#### Identification and Detection - Framework ####")
        print("##################################################")

    def __parse_gene(self, response):
        "Checks if is the correct gene."

        gene_code = {"1": "ERG11", "2": "FKS1", "3": "FKS2"}
        for code, gene in gene_code.items():
            if response == code:
                return gene

        return False

    def __parse_response(self, response, default="y"):
        "Parses the response given by the user."

        return (
            response == default.lower() or response == default.upper() or response == ""
        )

    def __parse_specie(self, response):
        "Checks if is the correct specie."

        specie_code = {
            "1": "Candida albicans",
            "2": "Candida glabrata",
            "3": "Candida tropicalis",
            "4": "Candida parapsilosis",
        }
        for code, specie in specie_code.items():
            if response == code:
                return specie

        return False

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

    def __show_status(self, response):
        response_code = {
            "ID-1": "Specie identification was executed with sucess. Please check the results.",
            "ID-0": "It wasn't possible execute the specie identification. ",
            "ANTI-1": "Antifungal resistance detection was executed with sucess. Please check the results.",
            "ANRI-0": "Is wasn't possible execute the detection of antifungal resistance.",
        }
        for code, action in response_code.items():
            if response == code:
                print(action)

    def __user_options(self):
        "The user responds to the form and gets the parameters."

        question = input("Test mode [y|N]: ")
        response = self.__parse_response(question)
        if response:
            params, should_exit = self.__mock_options()

            return params, should_exit

        else:
            while True:
                params = {}
                should_exit = False

                question = input("Identify specie [Y|n]:")
                response = self.__parse_response(question)
                if response:
                    params[ParameterKeys.IDENTIFICATION_KEY] = response
                    filepath_identification = input("File directory: ")
                    if valid_path(filepath_identification):
                        params[ParameterKeys.FILEPATH_IDENTIFICATION] = convert_path(
                            filepath_identification
                        )
                    else:
                        raise WrongFilePath
                        break

                question = input("Detect mutations? [Y|n]: ")
                response = self.__parse_response(question)
                if response:
                    params[ParameterKeys.MUTATION_KEY] = response
                    filepath_detection = input("File directory: ")
                    if valid_path(filepath_detection):
                        params[ParameterKeys.FILEPATH_DETECTION] = convert_path(
                            filepath_detection
                        )
                    else:
                        raise WrongFilePath
                        break

                    response = str(
                        input(
                            "Choose the specie:\n 1. C. albicans\n 2. C. glabrata\n 3. C. parapsilosis\n 4. C. tropicalis\n"
                        )
                    ).strip()
                    specie_name = self.__parse_specie(response)
                    if specie_name:
                        params[ParameterKeys.SPECIE_NAME] = specie_name
                    else:
                        raise WrongSpecieError
                        break

                    response = str(
                        input("Choose the gene:\n 1. ERG11\n 2. FKS1\n 3. FKS2\n")
                    ).strip()
                    gene_name = self.__parse_gene(response)
                    if gene_name:
                        params[ParameterKeys.GENE_NAME] = gene_name
                    else:
                        raise WrongGeneError
                        break

                    forward_primer = input("Forward primer: ").upper()
                    if valid_primer(forward_primer):
                        params[ParameterKeys.FORWARD_PRIMER] = forward_primer
                    else:
                        raise WrongPrimerError
                        break

                    reverse_primer = input("Reverse primer: ").upper()
                    if valid_primer(reverse_primer):
                        params[ParameterKeys.REVERSE_PRIMER] = reverse_primer
                    else:
                        raise WrongPrimerError
                        break

                response = input("Will you continue executing other pipelines? [y|N]: ")
                should_exit = self.__parse_response(response, default="n")

                return params, should_exit
