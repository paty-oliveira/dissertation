from framework.domain.IStep import IStep
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


class Read(IStep):

    """
        Allows the read  of the files with *.txt and *.fasta extensions.
    """

    def __init__(self, filepath):
        self.__file = filepath
        self.__readers = self.__add_readers()

    def execute(self):
        "Read the files according their extension."

        for reader in self.__readers:
            biological_sequences = reader.read(self.__file)

            if biological_sequences:
                return biological_sequences

    def __add_readers(self):
        "Adds the readers."

        list_readers = []
        list_readers.append(ReadFasta())
        list_readers.append(ReadTxt())

        return list_readers


class ReadFasta(IReadFile):

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

        return file_extension in ReadFasta.EXTENSIONS


class ReadTxt(IReadFile):

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

        return file_extension in ReadTxt.EXTENSIONS


class ReadCsv(IReadFile):

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

        return file_extension in ReadCsv.EXTENSIONS
