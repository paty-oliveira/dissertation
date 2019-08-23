from framework.domain.IStep import IStep
from framework.common.Utilities import valid_path
import shutil
import os
import subprocess


class Import(IStep):

    """
        Allows the importation of the file for the specific filepath. 
    """

    def __init__(self, filepath, data_folder):
        self.__filepath = filepath
        self.__data_folder = data_folder

    def execute(self):
        "Execute the importing of the files."

        try:
            if valid_path(self.__filepath):
                file = self.__import_file(self.__filepath, self.__data_folder)

        except FileNotFoundError as error:
            return error

    def __import_file(self, filepath, folder):
        "Copy files from path introduced by user to specific data folder."

        with os.scandir(filepath) as data_folder:
            for file in data_folder:
                shutil.copy(file, folder)
