from framework.domain.IStep import IStep
import requests
import os
import shutil

# Necessário fazer download da DB do Mardy para a pasta temporary/detection_mutation_proces
# sempre que o objeto AntifungalResistance for criado
# Criar em função auxiliar e chamar no construtor


# def download():
#     url = " http://mardy.dide.ic.ac.uk/session_files/DB_by_drug.csv"
#     data_folder = "framework/temporary/detection_mutation_process/"
#     request = requests.get(url, allow_redirects=True)
#     with open("DB_by_drug.csv", "wb") as output_file:
#         output_file.write(request.content)
#         # shutil.copy(output_file, data_folder)


class AntifungalResistance(IStep):

    """
        It allows the identification of antifungal resistance, through the 
        association of the mutations identified and the information of Mardy Database.
    """

    def __init__(self, reference_data, list_mutations):
        self.__reference_data = reference_data
        self.__mutations = list_mutations
        # download()

    def execute(self):
        "Verifies the presence of antifungal resistance."

        antifungal_resistance = self.__identify(self.__reference_data)

        if antifungal_resistance:
            return antifungal_resistance

        return "No antifungal resistance identified."

    def __identify(self, reference_data):
        "Identifies the antifungals according to the antifungal resistance promoted by the mutations."

        return [
            elements[0]
            for mutation in self.__mutations
            for elements in reference_data
            if mutation in elements[1]
        ]
