from framework.domain.IFileReader import IFileReader
import os
import re

class TXTReader(IFileReader):
    
    EXTENSIONS = ['.txt']

    def __is_extension(self, file):
        file_name, file_extension = os.path.splitext(file)
        return file_extension in TXTReader.EXTENSIONS

    def read(self, file):
        if self.__is_extension(file):
            list_sequences = []
            sequence = ''
            id_sequence = ''

            with open(file, 'r') as output_file:
                for line in output_file:
                    header = re.search(r'^>\w+', line)
                    
                    if header:
                        id_sequence = line.rstrip('\n')
                    
                    else:
                        sequence += line.replace('\n', '')
                
                list_sequences.append((id_sequence, sequence))
            
            return list_sequences
        
        return False