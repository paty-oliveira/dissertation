from framework.domain.IStep import IStep
from framework.common.Utilities import preffix, suffix

class SequenceTrimmed(IStep):

    """
        It allows the trimming of the sequence.
    """
    
    def __init__(self, query_sequence, reference_sequence, limit_number):
        self.__query_sequence = query_sequence
        self.__reference_sequence = reference_sequence
        self.__constraint = limit_number

    def execute(self):
        "Executes the trimms of sequence."

        for name, sequence in self.__reference_sequence.items():
            new_sequence = self.__trims(self.__query_sequence, sequence, self.__constraint)
            
            if new_sequence:
                return new_sequence

    def __trims(self, query_sequence, reference_sequence, constraint):
        "Trims the sequence according the constraints."

        start_sequence = preffix(query_sequence, constraint)
        end_sequence = suffix(query_sequence, constraint)

        if start_sequence and end_sequence in reference_sequence:
            initial_pos = reference_sequence.index(start_sequence)
            final_pos = reference_sequence.index(end_sequence) + len(end_sequence)
            trimmed_sequence = reference_sequence[initial_pos:final_pos]

            return trimmed_sequence

        return False

    
