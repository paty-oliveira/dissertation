from framework.common.ParameterKeys import ParameterKeys
from framework.application.BuildDataFlow import BuildDataFlow
from framework.presentation.IUserInterface import IUserInterface
import sys
import subprocess


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

            if should_exit:
                break

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
            ParameterKeys.REVERSE_PRIMER: "TTTTTA"
        }
        should_exit = True
        return params, should_exit

    def __parse_response(self, response, default="y"):
        "Parses the response given by the user."

        return (
            response == default.lower() or response == default.upper() or response == ""
        )

    def __headline(self):
        "Prints the headline of the framework."

        print("##################################################")
        print("# Identification and Detection - Framework ")
        print("##################################################")

    def __user_options(self):
        "The user responds to the form and gets the parameters."

        should_exit = False
        params = {}

        response = input("Test mode [y|N]: ")
        if self.__parse_response(response):
            params, should_exit = self.__mock_options()

            return params, should_exit

        else:
            response = input("Identify specie [Y|n]:")
            params[ParameterKeys.IDENTIFICATION_KEY] = self.__parse_response(response)
            if self.__parse_response(response):
                filepath_identification = input("File directory: ")
                params[ParameterKeys.FILEPATH_IDENTIFICATION] = convert_path(
                    filepath_identification
                )

            response = input("Detect mutations? [Y|n]: ")
            params[ParameterKeys.MUTATION_KEY] = self.__parse_response(response)
            if self.__parse_response(response):
                filepath_detection = input("File directory: ")
                params[ParameterKeys.FILEPATH_DETECTION] = convert_path(
                    filepath_detection
                )

                specie_name = input("Specie name: ").capitalize()
                params[ParameterKeys.SPECIE_NAME] = specie_name

                gene_name = input("Gene: ").upper()
                params[ParameterKeys.GENE_NAME] = gene_name

                forward_primer = input("Forward primer: ").upper()
                params[ParameterKeys.FORWARD_PRIMER] = forward_primer

                reverse_primer = input("Reverse primer: ").upper()
                params[ParameterKeys.REVERSE_PRIMER] = reverse_primer

            response = input("Will you continue executing other pipelines? [y|N]: ")
            should_exit = self.__parse_response(response, default="n")

            return params, should_exit
