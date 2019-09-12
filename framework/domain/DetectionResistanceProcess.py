from framework.domain.IProcess import IProcess
from framework.common.ParameterKeys import ParameterKeys, ExecutionCode
from framework.domain.Resistance import Resistance
from framework.common.Utilities import add_elements


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
        self.__steps = self.__add_steps()

    def run(self):
        "Executes all the steps of the process."

        execution_codes = [step.execute() for step in self.__steps]

        return execution_codes

    def __add_steps(self):
        "Adds the steps of the process."

        steps = []
        steps.append(
            Resistance(
                self.__configuration,
                self.__filepath,
                self.__specie,
                self.__gene,
                self.__primers,
            )
        )

        return steps
