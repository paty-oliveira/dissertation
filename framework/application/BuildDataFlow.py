from framework.common.ParameterKeys import ParameterKeys
from framework.domain.IdentificationSpeciePipeline import IdentificationSpeciePipeline
from framework.domain.DetectionMutationsPipeline import DetectionMutationPipeline


class BuildDataFlow:

    """
        Logic of pipelines controllers.
        Receive configurations from the app settings.
        Execute the pipelines according parameters introduced in console or GUI mode.

    """

    def __init__(self, configuration):
        self.__config = configuration

    def execute(self, params):
        "Execute the pipelines according the parameters transmitted."

        if params[ParameterKeys.IDENTIFICATION_KEY]:
            result = IdentificationSpeciePipeline(self.__config, params).run()

            return result

        if params[ParameterKeys.MUTATION_KEY]:
            result = DetectionMutationPipeline(self.__config, params).run()

            return result
