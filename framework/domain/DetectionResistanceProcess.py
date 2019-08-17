from framework.domain.IProcess import IProcess
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.DetectionResistance import AntifungalResistancePipeline


def add_elements(first_element, second_element):
    "Add elements to a list."

    return list([first_element, second_element])


class DetectionResistanceProcess(IProcess):

    """
        Logic of the detection resistance process.
    """

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_DETECTION]
        self.__specie = params[ParameterKeys.SPECIE_NAME]
        self.__gene = params[ParameterKeys.GENE_NAME]
        self.__primers = add_elements(
            params[ParameterKeys.FORWARD_PRIMER], params[ParameterKeys.REVERSE_PRIMER]
        )
        self.__pipeline = self.__add_pipeline()

    def run(self):
        "Executes all the steps of the process."

        for pipeline in self.__pipeline:
            resistance = pipeline.run()

            if resistance:
                return resistance

            return "No antifungal resistance identified."

    def __add_pipeline(self):
        "Adds the steps of the process."

        steps = []
        steps.append(
            AntifungalResistancePipeline(
                self.__configuration,
                self.__filepath,
                self.__specie,
                self.__gene,
                self.__primers,
            )
        )

        return steps
