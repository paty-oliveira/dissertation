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
        "Executes the translation of dna sequences."

        return tuple([self.__translate(sequence) for sequence in self.__dna_sequence])

    def __translate(self, dna_sequence):
        "Tanslates dna sequences in amino acid sequences."

        if len(dna_sequence) % 3 == 0:
            coding_dna = Seq(dna_sequence, IUPAC.unambiguous_dna)
            aminoacid_sequence = coding_dna.translate()

        else:
            trim_char = len(dna_sequence) % 3
            coding_dna = Seq(dna_sequence[:-trim_char], IUPAC.unambiguous_dna)
            aminoacid_sequence = coding_dna.translate()

        return aminoacid_sequence
