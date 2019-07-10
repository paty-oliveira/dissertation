from framework.domain.IFileReader import IFileReader
from Bio import SeqIO
import os


class FASTAReader(IFileReader):
    EXTENSIONS = [".fa", ".fasta"]

    def __is_extension(self, file):
        file_name, file_extension = os.path.splitext(file)
        return file_extension in FASTAReader.EXTENSIONS

    def read(self, file):
        if self.__is_extension(file):
            list_sequences = []
            record = SeqIO.read(file, "fasta")
            id_sequence = str(record.id)
            sequence = str(record.seq)
            list_sequences.append((id_sequence, sequence))

            return list_sequences

        return False
