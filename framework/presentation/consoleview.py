from framework.common.ParameterKeys import ParameterKeys, ExecutionCode
from framework.common.Utilities import execution_status, convert_path
from framework.application.BuildDataFlow import BuildDataFlow
from framework.presentation.IUserInterface import IUserInterface


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

            result = self.__controller.execute(params)
            print(execution_status(result, ExecutionCode.message))

            if should_exit:
                break

    def __boolean_question(
        self, question_1, question_2, response, key_1, key_2, params
    ):
        response = self.__boolean_option(question_1, response)
        params[key_1] = response
        if response:
            answer = self.__open_option(question_2, response)
            params[key_2] = convert_path(answer)

        return params

    def __boolean_option(self, question, response, default="Y"):
        answer = self.__open_option(question, response)
        return answer == default.lower() or answer == default.upper() or answer == ""

    def __choice_question(self, question, response, menu, key, params):
        response = self.__option_with_menu(question, menu, response)
        params[key] = response

        return params

    def __headline(self):
        "Prints the headline of the framework."

        print("##################################################")
        print("#### Identification and Detection - Framework ####")
        print("##################################################")

    def __open_question(self, question, response, key, params):
        response = self.__open_option(question, response)
        params[key] = response

        return params

    def __open_option(self, question, response):
        answer = ""
        while not answer:
            answer = input(question).strip()
            if not answer:
                print(response)
                answer = ""
        return answer

    def __option_with_menu(self, question, menu, response):
        option = ""
        while not option:
            for key, value in menu.items():
                print("{} - {}".format(key, value))
            option = input(question).strip()

            if option in menu.keys():
                option = menu[option]

            else:
                print(response)
                option = ""

        return option

    def __user_options(self):
        params = {}

        params = self.__boolean_question(
            "Identify specie [Y|n]:",
            "File directory: ",
            "This is not valid. Please try again!",
            ParameterKeys.IDENTIFICATION_KEY,
            ParameterKeys.FILEPATH_IDENTIFICATION,
            params,
        )
        params = self.__boolean_question(
            "Detect mutations? [Y|n]: ",
            "File directory: ",
            "This is not valid. Please try again!",
            ParameterKeys.MUTATION_KEY,
            ParameterKeys.FILEPATH_DETECTION,
            params,
        )
        if params[ParameterKeys.MUTATION_KEY]:
            params = self.__choice_question(
                "Choose the specie: ",
                "Please introduces a valid specie.",
                {
                    "1": "Candida albicans",
                    "2": "Candida glabrata",
                    "3": "Candida parapsilosis",
                    "4": "Candida tropicalis",
                },
                ParameterKeys.SPECIE_NAME,
                params,
            )
            params = self.__choice_question(
                "Choose the gene: ",
                "Please introduces a valid gene.",
                {"1": "ERG11", "2": "FKS1", "3": "FKS2"},
                ParameterKeys.GENE_NAME,
                params,
            )
            params = self.__open_question(
                "Forward primer: ",
                "Please introduces a valid primer.",
                ParameterKeys.FORWARD_PRIMER,
                params,
            )
            params = self.__open_question(
                "Reverse primer: ",
                "Please introduces a valid primer.",
                ParameterKeys.REVERSE_PRIMER,
                params,
            )
        should_exit = self.__boolean_option(
            "Will you continue executing other pipelines? [y|N]: ",
            "This is not valid. Please try again.",
            "N",
        )

        return params, should_exit

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
