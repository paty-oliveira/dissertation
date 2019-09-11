from framework.common.ParameterKeys import ParameterKeys
from framework.presentation.ResponseExecutionCode import ResponseExecutionCode
from framework.common.Utilities import execution_status, convert_path
from framework.presentation.IUserInterface import IUserInterface


class Question:
    SPECIE_IDENTIFICATION = "Identify specie [Y|n]: "
    ANTIFUNGAL_DETECTION = "Detect antifungal resistance? [Y|n]:  "
    FILEPATH = "File directory: "
    SPECIE = "Choose the specie: "
    GENE = "Choose the gene: "
    FORWARD_PRIMER = "Forward primer: "
    REVERSE_PRIMER = "Reverse primer: "
    PIPELINE_CONTINUATION = "Will you continue executing other pipelines? [y|N]: "


class Menu:
    GENES = {"1": "ERG11", "2": "FKS1", "3": "FKS2"}
    SPECIES = {
        "1": "Candida albicans",
        "2": "Candida glabrata",
        "3": "Candida parapsilosis",
        "4": "Candida tropicalis",
    }


class Response:
    GENERAL = "This is not valid. Please try again!"
    SPECIE_RESPONSE = "Please introduces a valid specie."
    GENE_RESPONSE = "Please introduces a valid gene."
    PRIMER_RESPONSE = "Please introduces a valid primer."


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
            params, should_exit = self.__mock_options()
            print("\nRunning pipeline...")

            result = self.__controller.execute(params)
            print(execution_status(result, ResponseExecutionCode.STATUS))

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
        params[key] = response.upper()

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
            Question.SPECIE_IDENTIFICATION,
            Question.FILEPATH,
            Response.GENERAL,
            ParameterKeys.IDENTIFICATION_KEY,
            ParameterKeys.FILEPATH_IDENTIFICATION,
            params,
        )
        params = self.__boolean_question(
            Question.ANTIFUNGAL_DETECTION,
            Question.FILEPATH,
            Response.GENERAL,
            ParameterKeys.DETECTION_KEY,
            ParameterKeys.FILEPATH_DETECTION,
            params,
        )
        if params[ParameterKeys.DETECTION_KEY]:
            params = self.__choice_question(
                Question.SPECIE,
                Response.SPECIE_RESPONSE,
                Menu.SPECIES,
                ParameterKeys.SPECIE_NAME,
                params,
            )
            params = self.__choice_question(
                Question.GENE,
                Response.GENE_RESPONSE,
                Menu.GENES,
                ParameterKeys.GENE_NAME,
                params,
            )
            params = self.__open_question(
                Question.FORWARD_PRIMER,
                Response.PRIMER_RESPONSE,
                ParameterKeys.FORWARD_PRIMER,
                params,
            )
            params = self.__open_question(
                Question.REVERSE_PRIMER,
                Response.PRIMER_RESPONSE,
                ParameterKeys.REVERSE_PRIMER,
                params,
            )
        should_exit = self.__boolean_option(
            Question.PIPELINE_CONTINUATION, Response.GENERAL, "N"
        )

        return params, should_exit

    def __mock_options(self):
        "Represents a dictionary with parameters for test mode."

        params = {
            ParameterKeys.IDENTIFICATION_KEY: False,
            ParameterKeys.DETECTION_KEY: True,
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
