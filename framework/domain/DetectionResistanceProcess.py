from framework.domain.IProcess import IProcess
from framework.common.ParameterKeys import ParameterKeys
from framework.domain.DetectionResistance import DetectionResistance


def put_element_into_list(string):
    return [element for element in string.split(" ")]


class DetectionResistanceProcess(IProcess):
    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__filepath = params[ParameterKeys.FILEPATH_DETECTION]
        self.__specie = params[ParameterKeys.SPECIE_NAME]
        self.__gene = params[ParameterKeys.GENE_NAME]
        self.__primer = put_element_into_list(params[ParameterKeys.PRIMERS])
        self.__steps = self.__add_step()

    def run(self):
        for step in self.__steps:
            resistance = step.execute()

            if resistance:
                return resistance

    def __add_step(self):
        steps = []

        steps.append(
            DetectionResistance(
                self.__configuration,
                self.__filepath,
                self.__specie,
                self.__gene,
                self.__primer,
            )
        )

        return steps
