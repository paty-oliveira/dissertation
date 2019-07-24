from framework.domain.IStep import IStep
from framework.domain.ExtractInformation import get_preffix, get_suffix
import re

class RemoveSequence(IStep):

    def remove_primers(self, sequence, list_primers):
        return re.sub(r"|".join(map(re.escape, list_primers)), "", sequence)


    def trim_sequence(self, reference_sequence, subject_sequence):
        start_sequence = get_preffix(subject_sequence)
        end_sequence = get_suffix(subject_sequence)

        if start_sequence and end_sequence in reference_sequence:
            initial_pos = reference_sequence.index(start_sequence)
            final_pos = reference_sequence.index(end_sequence) + len(end_sequence)
            trimmed_sequence = reference_sequence[initial_pos:final_pos]

            return trimmed_sequence

        return False

