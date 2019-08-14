import os
import argparse
import shutil
import urllib.request
from framework.application.BuildDataFlow import BuildDataFlow
from framework.presentation.ConsoleView import ConsoleView
from framework.presentation.GuiView import GuiView
from framework.common.ParameterKeys import ParameterKeys


class Application:

    """
        Logic of start of the framework.
    """

    def __init__(self, configuration):
        self.__configuration = configuration
        self.__args_parser = self.__configure_arguments()
        self.__tmp_folder_path = self.__configuration.get_path_root_folder()
        self.__url = self.__configuration.get_url()
        self.__filename = self.__configuration.get_file_name()
        self.__filepath = self.__configuration.get_path_detection_resistance_process()
        self.__prepare_environment()
        self.__download(self.__url, self.__filename, self.__filepath)

    def start(self):
        "This is the initialization of the application, throught the modes selected by user."
        try:
            print(self.__configuration.get_initial_message())

            args = self.__args_parser.parse_args()
            params = vars(args)

            if self.__is_mode(params["mode"], "console"):
                self.run_console()

            elif self.__is_mode(params["mode"], "gui"):
                self.run_gui()

            else:
                self.run_batch_mode(params)

            self.__removal_folder_content(self.__tmp_folder_path)

            print(self.__configuration.get_final_message())
        
        except Exception as error:
            print("Error during the execution of the application. Please try again.", error)

    def run_console(self):
        "This is the default behavior. The application calls the console view."

        controller = BuildDataFlow(self.__configuration)
        view = ConsoleView(controller)
        view.show()

    def run_gui(self):
        "The application calls the gui view."

        controller = BuildDataFlow(self.__configuration)
        view = GuiView(controller)
        view.show()

    def run_batch_mode(self, params):
        "Runs the application in batch mode."

        controller = BuildDataFlow(self.__configuration)
        controller.execute(params)

    def __configure_arguments(self):
        "Configures the arguments accepted by the application."

        parser = argparse.ArgumentParser(
            description="Pipeline for identification of Candida species and detection of antifungal resistance"
        )

        parser.add_argument(
            "-i",
            nargs="?",
            const="console",
            default="batch",
            choices=["console", "gui", "batch"],
            metavar="console, gui, batch",
            dest="mode",
            help="Defines the mode to run the pipeline",
        )

        parser.add_argument(
            "-file_ident",
            nargs="?",
            dest=ParameterKeys.FILEPATH_IDENTIFICATION,
            default="",
            const="",
            metavar="filepath",
            help="Imports file and generates dataset for identification process",
        )

        parser.add_argument(
            "-file_detect",
            nargs="?",
            dest=ParameterKeys.FILEPATH_DETECTION,
            default="",
            const="",
            metavar="filepath",
            help="Imports file for detection of mutations.",
        )

        parser.add_argument(
            "-id",
            action="store_true",
            dest=ParameterKeys.IDENTIFICATION_KEY,
            help="Identifies the specie on the dataset",
        )

        parser.add_argument(
            "-d",
            action="store_true",
            dest=ParameterKeys.MUTATION_KEY,
            help="Detects mutation from the dataset",
        )

        return parser

    def __download(self, url, file_name, path):
        "Executes the download of the file from specific URL.."

        try:
            filepath = os.path.join(path, file_name)
            urllib.request.urlretrieve(url, filepath)

        except ConnectionRefusedError as error:
            print("Connection error with the HTTP connection: ", error)

    def __is_mode(self, base_mode, mode):
        "Verifies if the arguments contain the given mode."

        return base_mode == mode.lower() or base_mode == mode.upper()

    def __prepare_environment(self):
        "Prepares environment of execution before the start of the application."

        tmp_folder = self.__configuration.get_path_root_folder()
        identification_process_folder = (
            self.__configuration.get_path_identification_process()
        )
        data_folder_identification = (
            self.__configuration.get_path_data_folder_identification()
        )
        detection_resistance_process = (
            self.__configuration.get_path_detection_resistance_process()
        )

        if not os.path.exists(tmp_folder):
            os.mkdir(tmp_folder)

        if not os.path.exists(identification_process_folder):
            os.mkdir(identification_process_folder)

        if not os.path.exists(data_folder_identification):
            os.mkdir(data_folder_identification)

        if not os.path.exists(detection_resistance_process):
            os.mkdir(detection_resistance_process)

    def __removal_folder_content(self, path_folder):
        "Removes all files and directories in a specific folder."

        with os.scandir(path_folder) as items:
            for item in items:

                if os.path.isfile(item):
                    os.remove(item)

                elif os.path.isdir(item):
                    shutil.rmtree(item)
