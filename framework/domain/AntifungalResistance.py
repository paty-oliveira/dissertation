from framework.domain.IStep import IStep


class AntifungalResistance(IStep):

    """
        It allows the identification of antifungal 
        resistance, through the association of the
        mutations identified and the information of Mardy Database.
    """

    def __init__(self, reference_data, list_mutations):
        self.__reference_data = reference_data
        self.__mutations = list_mutations

    def execute(self):
        "Verifies the presence of antifungal resistance."

        antifungal_resistance = self.__identify(self.__reference_data)

        if antifungal_resistance:
            return antifungal_resistance

        return False

    def __identify(self, reference_data):
        """Identifies the antifungals according to the 
        antifungal resistance promoted by the mutations.
        """

        return [
            elements[0]
            for mutation in self.__mutations
            for elements in reference_data
            if mutation in elements[1]
        ]
