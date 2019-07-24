from framework.domain.IStep import IStep
from framework.domain.ReadFile import ReadCsv
import pandas as pd

class ExtractInformation(IStep):
    
    """
        It allows the extraction of specific information from files.
    """
    
    def __init__(self, configuration, specie, gene):
        self.__filepath = configuration.get_antifungal_genes_file()
        self.__file_reader = ReadCsv(self.__filepath)
        self.__specie = specie
        self.__gene = gene

    def execute(self):
        dna_sequence, dna_position = self.__retrieve_reference_fields()

        return dna_sequence, dna_position

    def __retrieve_reference_fields(self):
        "Obtains the information about dna sequence and dna position of the reference gene and specie."

        dataframe = self.__file_reader
        dataframe.set_index("Specie", inplace=True)

        subdata_specie = dataframe.loc[self.__specie]

        dna_sequence = subdata_specie.loc[
            subdata_specie["Gene"] == self.__gene, "Sequence"
        ].to_dict()

        dna_position = subdata_specie.loc[
            subdata_specie["Gene"] == self.__gene, "Initial position"
        ].to_dict()

        return dna_sequence, dna_position


    
