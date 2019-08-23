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

    def __headline(self):
        "Prints the headline of the framework."

        print("##################################################")
        print("#### Identification and Detection - Framework ####")
        print("##################################################")

    def __open_option(self, question, response):
        answer = ""
        while not answer:
            answer = input(question).strip()
            if not answer:
                print(response)
            
        return answer

    def __boolean_option(self, question, response, default="Y"):
        answer = self.__open_option(question, response)
        return answer == default.lower() or answer == default.upper() or answer == ""

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

        response = self.__boolean_option("Identify specie [Y|n]:", "This is not valid. Please try again!")
        params[ParameterKeys.IDENTIFICATION_KEY] = response
        if response:
            identification_filepath = self.__open_option("File directory: ", "Please introduces a valid path.")
            params[ParameterKeys.FILEPATH_IDENTIFICATION] = convert_path(identification_filepath)

        response = self.__boolean_option("Detect mutations? [Y|n]: ", "This is not valid. Please try again!")
        params[ParameterKeys.MUTATION_KEY] = response
        if response:
            detection_filepath = self.__open_option("File directory: ", "Please introduces a valid path")
            params[ParameterKeys.FILEPATH_DETECTION] = convert_path(detection_filepath)
        
            specie = self.__option_with_menu("Choose the specie:", {
                "1": "Candida albicans",
                "2": "Candida glabrata",
                "3": "Candida parapsilosis",
                "4": "Candida tropicalis"
            }, "Please introduces a valid specie." )
            params[ParameterKeys.SPECIE_NAME] = specie

            gene = self.__option_with_menu("Choose the gene:", {
                "1": "ERG11", 
                "2": "FKS1", 
                "3": "FKS2"
            }, "Please introduces a valid gene.")
            params[ParameterKeys.GENE_NAME] = gene

            forward_primer = self.__open_option("Forward primer: ", "Please introduces a valid primer.")
            params[ParameterKeys.FORWARD_PRIMER] = forward_primer

            reverse_primer = self.__open_option("Reverse primer: ", "Please introduces a valid primer.")
            params[ParameterKeys.REVERSE_PRIMER] = reverse_primer
        
        should_exit = self.__boolean_option("Will you continue executing other pipelines? [y|N]: ", "This is not valid. Please try again.", "N")
        
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

