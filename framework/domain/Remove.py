from framework.domain.IStep import IStep
from framework.domain.Extract import Extract
import re


def preffix(string):
    "Returns the first 11 characters of the string."

    return string[0:11]


def suffix(string):
    "Returns the last 11 characters of the string."

    return string[-11:]


class Remove(IStep):

    """
        It allows the removal of subsequences from reference sequence.
    """

    def __init__(self, sbjct_sequence, ref_sequence, primers):
        self.__sbjct_sequence = sbjct_sequence
        self.__ref_sequence = ref_sequence
        self.__primers = primers

    def execute(self):
        "Executes the removal of primers and generation of the trimmed reference sequence."

        sbjct_sequence_trimmed = self.__remove(self.__sbjct_sequence, self.__primers)

        for name, sequence in self.__ref_sequence.items():
            ref_sequence_trimmed = self.__trims(sequence, sbjct_sequence_trimmed)

        return sbjct_sequence_trimmed, ref_sequence_trimmed

    def __remove(self, sequence, primers):
        "Removes substrings of the string."

        return re.sub(r"|".join(map(re.escape, primers)), "", sequence)

    def __trims(self, reference_sequence, subject_sequence):
        "Trims the sequence according the constraints."

        start_sequence = preffix(subject_sequence)
        end_sequence = suffix(subject_sequence)

        if start_sequence and end_sequence in reference_sequence:
            initial_pos = reference_sequence.index(start_sequence)
            final_pos = reference_sequence.index(end_sequence) + len(end_sequence)
            trimmed_sequence = reference_sequence[initial_pos:final_pos]

            return trimmed_sequence

        return False
