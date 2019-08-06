from framework.domain.IStep import IStep


class Mutation(IStep):

    """
        It allows the identification of mutations present in amino acid sequences.
    """

    def __init__(self, seq_aa_reference, seq_aa_subject, initial_pos):
        self.__aminoacid_ref = seq_aa_reference
        self.__aminoacid_sbjct = seq_aa_subject
        self.__initial_pos = initial_pos

    def execute(self):
        "Executes the detection of mutations present in the sequence."

        if not self.__is_equal(self.__aminoacid_ref, self.__aminoacid_sbjct):
            aminoacid_mutations = self.__sequence_alterations()

            return aminoacid_mutations

        return []

    def __sequence_alterations(self):
        "Identifies the alterations present in the sequences."

        for specie, initial_pos in self.__initial_pos.items():
            return [
                (
                    self.__aminoacid_ref[position],
                    initial_pos + position,
                    self.__aminoacid_sbjct[position],
                )
                for position in range(len(self.__aminoacid_ref))
                if self.__aminoacid_ref[position] != self.__aminoacid_sbjct[position]
            ]

    def __is_equal(self, reference_sequence, subject_sequence):
        "Verifies if two sequences are equals."
        
        return str(reference_sequence) == str(subject_sequence)
