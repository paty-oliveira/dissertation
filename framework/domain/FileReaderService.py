from framework.domain.FASTAReader import FASTAReader
from framework.domain.TXTReader import TXTReader
from framework.common.aux_functions import find_files
import os

class FileReaderService:
    
    def __init__(self, filepath):
        self.__files = find_files(filepath)
        self.__readers = self.__add_readers()

    def __add_readers(self):
        list_readers = []
        list_readers.append(FASTAReader())
        list_readers.append(TXTReader())

        return list_readers

    def read(self):
        results = {}

        for file in self.__files:
            for reader in self.__readers:
                biological_sequences = reader.read(file)

                if biological_sequences:
                    results[os.path.basename(file)] = biological_sequences
        
        return results




    