from framework.domain.IIdentificationProcess import IIdentificationProcess 
import subprocess

class PIPITSSequencePreparation(IIdentificationProcess):
    
    '''
        Represent the PIPITS_PREP step from PIPITS.
        
        And execute the commands of this step.

    '''

    cmd_args_readpairlist = ["pispino_createreadpairslist", "-i", "rawdata", "-o", "readpairslist.txt"]

    cmd_args_sequenceprep = ["pispino_seqprep", "-i", "rawdata", "-o", "out_seqprep", "-l", "readpairslist.txt"]


    def __init__(self, configuration):
        self.__configuration = configuration
        self.__root_folder = self.__configuration.get_path_identification_process()


    def is_success(self, process):
        'Verify if the subprocess called happened.'
        
        return process == 0 


    def run_commands(self):
        'Execute all commands of each subprocess called.'

        if True:
            self.__generate_read_pairs_list()

            self.__preprocessing_sequence()
        
        else:
            pass
        

    def __generate_read_pairs_list(self):
        'Create read pair list file throught the subprocess of PIPITS.'

        process_to_execute = subprocess.call(PIPITSSequencePreparation.cmd_args_readpairlist, 
                            cwd=self.__root_folder)

        if self.is_success(process_to_execute):
            return True


    def __preprocessing_sequence(self):
        'Preprocess the sequencing files throught the subprocess of PIPITS.'

        process_to_execute = subprocess.call(PIPITSSequencePreparation.cmd_args_sequenceprep, 
                            cwd=self.__root_folder)

        if self.is_success(process_to_execute):
            return True


