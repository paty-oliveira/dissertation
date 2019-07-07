from framework.domain.pipeline import Pipeline

class PipelineController:

    '''
        Logic of pipeline controller.

        Receive configurations from the app settings.

        Execute the pipeline according parameters introduced in console or GUI mode.

    '''
    def __init__(self, configuration):
        self.__config = configuration


    def execute(self, params):
        'Execute pipeline according the parameters transmitted.'
        
        pipeline = Pipeline(self.__config, params)
    
        pipeline.run()

        

