from framework.domain.IStep import IStep
from framework.exceptions.exceptions import FileReadindError
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
        
        file = self.__import_file()
        return file

    def __import_file(self):
        "Copy files from path introduced by user to specific data folder."

        with os.scandir(self.__filepath) as data_folder:
            for file in data_folder:
                shutil.copy(file, self.__data_folder)
