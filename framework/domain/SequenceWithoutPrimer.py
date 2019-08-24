from framework.domain.IStep import IStep
from framework.common.Utilities import valid_string
import re


class SequenceWithoutPrimer(IStep):

    """
        It allows the removal of primers in sequence.
    """

    def __init__(self, sequence, primers, alphabet):
        self.__sequence = sequence
        self.__primers = primers
        self.__alphabet = alphabet

    def execute(self):
        "Executes the removal of primers."

        if valid_string(self.__primers, self.__alphabet):
            new_sequence = self.__remove(self.__sequence, self.__primers)

            return new_sequence

        return False

    def __remove(self, sequence, primers):
        "Removes substrings of the string."

        return re.sub(r"|".join(map(re.escape, primers)), "", sequence)
