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
        self.__params = params
        self.__execution = params[ParameterKeys.DETECTION_KEY]
        self.__filepath = ""
        self.__specie = ""
        self.__gene = ""
        self.__primers = ""

    def run(self):
        "Executes all the steps of the process."

        if self.__execution:
            self.__filepath = self.__params[ParameterKeys.FILEPATH_DETECTION]
            self.__specie = self.__params[ParameterKeys.SPECIE_NAME]
            self.__gene = self.__params[ParameterKeys.GENE_NAME]
            self.__primers = add_elements(
                self.__params[ParameterKeys.FORWARD_PRIMER], 
                self.__params[ParameterKeys.REVERSE_PRIMER]
            )
            steps = self.__add_steps()
            execution_codes = [step.execute() for step in steps]

            return execution_codes
        
        else:
            pass

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
