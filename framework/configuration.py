import configparser


class Configuration:

    def __init__(self, filename):
        self.__parser = configparser.ConfigParser()
        self.__parser.read(filename)

    
    def get_path_root_folder(self):
        return self.__parser.get('IDENTIFICATIONPROCESS', 'root_folder')

    def get_path_identification_process(self):
        return self.__parser.get('IDENTIFICATIONPROCESS', 'identification_folder')

    def get_path_data_folder_identification(self):
        return self.__parser.get('IDENTIFICATIONPROCESS', 'data_folder_identification')

    def get_phylotype_table_results(self):
        return self.__parser.get('IDENTIFICATIONPROCESS', 'phylotype_results_folder')
    
    def get_file_preprocessed(self):
        return self.__parser.get('IDENTIFICATIONPROCESS', 'fasta_file_prepped')

    def get_path_detection_mutation_process(self):
        return self.__parser.get('DETECTIONMUTATIONPROCESS', 'detection_mutation_folder')

    def get_path_data_folder_mutation(self):
        return self.__parser.get('DETECTIONMUTATIONPROCESS', 'data_folder_mutation')

    def get_initial_message(self):
        return self.__parser.get('MESSAGES', 'inicial_message')

    def get_final_message(self): 
        return self.__parser.get('MESSAGES', 'final_message')
