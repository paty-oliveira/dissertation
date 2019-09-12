from framework.common.ParameterKeys import ParameterKeys
from framework.domain.IdentificationSpecieProcess import IdentificationSpecieProcess
from framework.domain.DetectionResistanceProcess import DetectionResistanceProcess


class RunProcessController:

    """
        Logic of processes controllers.
        Receive configurations from the app settings.
        Execute the process according parameters introduced in console or GUI mode.

    """

    def __init__(self, configuration):
        self.__configuration = configuration

    def execute_specie_identification(self, params):

        result = IdentificationSpecieProcess(self.__configuration, params).run()

        return result

    def execute_antifungal_resistance_detection(self, params):

        result = DetectionResistanceProcess(self.__configuration, params).run()

        return result
