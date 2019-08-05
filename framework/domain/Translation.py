from framework.domain.IStep import IStep
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


class Translation(IStep):

    """
        It allows the translation of the dna sequence into amino acid sequence.
    """

    def __init__(self, dna_sequence):
        self.__dna_sequence = dna_sequence

    def execute(self):
        return tuple([self.__translate(sequence) for sequence in self.__dna_sequence])

    def __translate(self, dna_sequence):
        coding_dna = Seq(dna_sequence, IUPAC.unambiguous_dna)
        aminoacid_sequence = coding_dna.translate()

        return aminoacid_sequence
