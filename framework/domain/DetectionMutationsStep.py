from framework.domain.IStep import IStep
from framework.domain.ImportSequencingFile import ImportSequecingFile
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.FileReaderService import FileReaderService
from framework.domain.ReportWriter import ReportWriter
from framework.domain.Mutation import Mutation


class DetectionMutationStep(IStep):
    
    '''
        Allows detect the mutations presente in the dataset.
    '''

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__params = params
        self.__execution = params[ParameterKeys.MUTATION_KEY]
        self.__data_folder = self.__configuration.get_path_data_folder_mutation()

    def execute(self):
        if self.__execution:
            filepath = self.__params[ParameterKeys.FILEPATH_DETECTION]
            importing_file = ImportSequecingFile(filepath, self.__data_folder).execute()

            dna_sequence = FileReaderService(self.__data_folder).read() #é um dicionário com key -> ficheiro, value -> (id_sequence, sequence)
            
            
            # mutations = Mutation().identify_alterations()
            # result = Mutation().get_antifungual_resistance(mutations)
            
            # if result:
            #     antifungal_resistant = self.__get_antifungal_results()
            #     antifungal_results = ReportWriter(filepath).write_mutations(antifungal_resistant)
            #     return antifungal_results



    # def __get_mutations_results(self):
    #     pass 




    