from framework.domain.IStep import IStep
from framework.domain.ExtractInformation import ExtractInformation
import re


def get_preffix(sequence):
    return sequence[0:11]


def get__suffix(sequence):
    return sequence[-11:]


class RemoveSequence(IStep):

    """
        It allows the removal of subsequences from reference sequence.
    """

    def __init__(self, sbjct_sequence, ref_sequence, primers):
        self.__sbjct_sequence = sbjct_sequence
        self.__ref_sequence = ref_sequence
        self.__list_primer = primers

    def execute(self):
        sbjct_sequence_trimmed = self.__remove_primers(
            self.__sbjct_sequence, self.__list_primer
        )

        for name, sequence in self.__ref_sequence.items():
            ref_sequence_trimmed = self.__trim_sequence(
                sequence, sbjct_sequence_trimmed
            )

        return sbjct_sequence_trimmed, ref_sequence_trimmed

    def __trim_sequence(self, reference_sequence, subject_sequence):
        start_sequence = get_preffix(subject_sequence)
        end_sequence = get__suffix(subject_sequence)

        if start_sequence and end_sequence in reference_sequence:
            initial_pos = reference_sequence.index(start_sequence)
            final_pos = reference_sequence.index(end_sequence) + len(end_sequence)
            trimmed_sequence = reference_sequence[initial_pos:final_pos]

            return trimmed_sequence

        return False

    def __remove_primers(self, sequence, list_primers):
        return re.sub(r"|".join(map(re.escape, list_primers)), "", sequence)
