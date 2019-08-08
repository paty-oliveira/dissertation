from framework.domain.IStep import IStep
from framework.domain.Read import ReadCsv
import pandas as pd


class Extract(IStep):

    """
        It allows the extraction of specific information from files.
    """

    def __init__(self, configuration, specie, gene):
        self.__ref_genes_file = configuration.get_antifungal_genes_file()
        self.__mardy_file = configuration.get_mardy_file()
        self.__file_reader = ReadCsv()
        self.__specie = specie
        self.__gene = gene

    def execute(self):
        "Executes the extraction of the reference fields."

        dna_sequence, dna_position = self.__sequence_position_reference()
        mardy_information = self.__drugs_mutations_reference()

        return dna_sequence, dna_position, mardy_information

    def __drugs_mutations_reference(self):

        dataframe = self.__file_reader.read(self.__mardy_file)
        dataframe.set_index("Organism", inplace=True)

        subdata_specie = dataframe.loc[self.__specie]

        subdata_antifungal = subdata_specie.loc[
            subdata_specie["Gene name"] == self.__gene, ["AA mutation", "Drug"]
        ]

        return set(
            [(value[1], value[0]) for index, value in subdata_antifungal.iterrows()]
        )

    def __sequence_position_reference(self):
        "Obtains the information about dna sequence and dna position of the reference gene and specie."

        dataframe = self.__file_reader.read(self.__ref_genes_file)
        dataframe.set_index("Specie", inplace=True)

        subdata_specie = dataframe.loc[self.__specie]

        dna_sequence = subdata_specie.loc[
            subdata_specie["Gene"] == self.__gene, "Sequence"
        ].to_dict()

        dna_position = subdata_specie.loc[
            subdata_specie["Gene"] == self.__gene, "Initial position"
        ].to_dict()

        return dna_sequence, dna_position
