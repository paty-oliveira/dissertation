from framework.domain.IStep import IStep

# Necessário fazer download da DB do Mardy para a pasta temporary/detection_mutation_proces
# sempre que o objeto AntifungalResistance for criado
# Criar em função auxiliar e chamar no construtor


def download():
    pass


def remove(file):
    pass


class AntifungalResistance(IStep):
    def __init__(self, reference_data, list_mutations):
        self.__reference_data = reference_data
        self.__mutations = list_mutations

    def execute(self):
        antifungal_resistance = self.__identify(self.__reference_data)

        if antifungal_resistance:
            return antifungal_resistance

        return "No antifungal resistance identified."

    def __identify(self, reference_data):
        return [
            elements[0]
            for mutation in self.__mutations
            for elements in reference_data
            if mutation in elements[1]
        ]
