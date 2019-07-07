import os
import shutil
import subprocess
from framework.domain.IdentificationStep import IdentificationStep
from framework.domain.DetectionMutationsStep import DetectionMutationStep
from framework.common.ParameterKeys import ParameterKeys

class Pipeline:
    '''
        Logic of the pipeline execution.

        The steps are executed if the boolean transmited throught
        parameters is True.

    '''

    def __init__(self, configuration, params):
        self.__configuration = configuration
        self.__steps = self._Pipeline__add_steps(params)
        



    def run(self):
        ' Execute the pipeline.'

        for step in self._Pipeline__steps:
            step.execute()
        

    def __add_steps(self, params):
        'Add steps for pipeline execution'
        
        steps = []
        
        steps.append(IdentificationStep(self.__configuration, params))
        steps.append(DetectionMutationStep(self.__configuration, params))

        return steps



