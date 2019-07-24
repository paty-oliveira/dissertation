from framework.domain.IStep import IStep

class Mutation(IStep):
    
    """
        It allows the identification of mutations present in amino acid sequences.
    """

    def __init__(self, seq_aa_reference, seq_aa_subject, initial_pos):
        self.__aa_reference = seq_aa_reference
        self.__aa_subject = seq_aa_subject
        self.__initial_pos = initial_pos

    def execute(self):
        if not self.__is_equal(self.__aa_reference, self.__aa_subject):
            aminoacid_mutations = self.__identify_substitutions()

            return aminoacid_mutations
        
        return []

    def __identify_substitutions(self):
        return [
            (
                self.__aa_reference[position],
                self.__initial_pos + position,
                self.__aa_subject[position]
            )
            for position in range(len(self.__aa_reference))
            if self.__aa_reference[position] != self.__aa_subject[position]
        ]

    
    def __is_equal(self, reference_sequence, subject_sequence):
        return str(reference_sequence) == str(subject_sequence)
