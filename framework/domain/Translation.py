from framework.domain.IStep import IStep
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


class Translation(IStep):

    """
        It allows the translation of the dna sequence into amino acid sequence.
    """

    def translate(self, dna_sequence):
        coding_dna = Seq(dna_sequence, IUPAC.unambiguous_dna)
        aminoacid_sequence = coding_dna.translate()

        return aminoacid_sequence
