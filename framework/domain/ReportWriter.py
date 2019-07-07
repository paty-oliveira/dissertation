import os



class ReportWriter:

    def __init__(self, results_path):
        self.__path = results_path

    def write_identification(self, results):
        'Writes a report with the result of PIPITS identification process in a *.txt file.'

        head = 'Identification of fungi species:\nNumber\tKindgom\tPhylo\tClass\tOrder\t Family\t Genus\t Specie\t\n'
        
        with open(os.path.join(self.__path), 'specie_identification.txt', 'w') as output_file:
            output_file.write(head)
            results.to_string(output_file)

    def write_mutations(self, results):
        'Writes a report with the results of the all mutations detected in a *.txt file.'
        pass
        
        # with open(os.path.join(self.__path, 'mutations.txt'), 'w') as output_file:
        #     for file, sequence_info in results.items():
        #         output_file.write(str(file))
