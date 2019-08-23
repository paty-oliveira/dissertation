from framework.domain.IStep import IStep
from framework.common.Utilities import valid_file
from abc import ABC, abstractmethod
import pandas as pd
import os
import re
from Bio import SeqIO


class IReadFile(ABC):

    """
        Interface that implements the read behavior.
    """

    @abstractmethod
    def read(self, file):
        pass


class FileReading(IStep):

    """
        Allows the read  of the files with *.txt and *.fasta extensions.
    """

    def __init__(self, filepath):
        self.__file = filepath
        self.__readers = self.__add_readers()

    def execute(self):
        "Read the files according their extension."

        try:
            for reader in self.__readers:
                if valid_file(self.__file):
                    biological_sequences = reader.read(self.__file)

                    if biological_sequences:
                        return biological_sequences

        except FileExistsError as error:
            return error

    def __add_readers(self):
        "Adds the readers."

        list_readers = []
        list_readers.append(FastaReading())
        list_readers.append(TxtReading())

        return list_readers


class FastaReading(IReadFile):

    EXTENSIONS = [".fa", ".fasta"]

    def read(self, file):
        "Read files with *.fasta extension."

        if self.__is_extension(file):
            record = SeqIO.read(file, "fasta")
            id_sequence = str(record.id)
            sequence = str(record.seq)

            return id_sequence, sequence

        return False

    def __is_extension(self, file):
        "Verify the file extension."

        file_name, file_extension = os.path.splitext(file)

        return file_extension in FastaReading.EXTENSIONS


class TxtReading(IReadFile):

    EXTENSIONS = [".txt"]

    def read(self, file):
        "Read files with *.txt extension."

        if self.__is_extension(file):
            sequence = ""
            id_sequence = ""

            with open(file, "r") as output_file:
                for line in output_file:
                    header = re.search(r"^>\w+", line)

                    if header:
                        id_sequence = line.rstrip("\n")

                    else:
                        sequence += line.replace("\n", "")

            return id_sequence, sequence

        return False

    def __is_extension(self, file):
        "Verify the file extension."

        file_name, file_extension = os.path.splitext(file)

        return file_extension in TxtReading.EXTENSIONS


class CsvReading(IReadFile):

    EXTENSIONS = [".csv"]

    def read(self, file, header):
        "Read files with *.csv extension."

        if self.__is_extension(file):
            dataframe = pd.read_csv(file, header=header)
            return dataframe

        return False

    def __is_extension(self, file):
        "Verify the file extension."

        file_name, file_extension = os.path.splitext(file)

        return file_extension in CsvReading.EXTENSIONS
