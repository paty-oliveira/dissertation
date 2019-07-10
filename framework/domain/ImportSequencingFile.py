from framework.domain.IStep import IStep
import shutil
import os
import subprocess


class ImportSequecingFile:

    """
        Allows import the sequencing file throught the filepath. 
    """

    def __init__(self, filepath, data_folder):
        self.__filepath = filepath
        self.__data_folder = data_folder

    def execute(self):
        "Execute the importing of sequencing files to temporary directory."
        if True:
            self.__import_files()

        else:
            pass

    def __import_files(self):
        "Copy files from path introduced by user to data folder in temporary directory"

        with os.scandir(self.__filepath) as data_folder:
            for file in data_folder:
                shutil.copy(file, self.__data_folder)
