from framework.domain.IStep import IStep


class Mutation(IStep):

    """
        It allows the identification of mutations present in amino acid sequences.
    """

    def __init__(self, ref_aminoacid, query_aminoacid, initial_pos):
        self.__ref_aminoacid = ref_aminoacid
        self.__query_aminoacid = query_aminoacid
        self.__initial_pos = initial_pos

    def execute(self):
        "Executes the detection of mutations present in the sequence."

        if not self.__is_equal(self.__ref_aminoacid, self.__query_aminoacid):
            aminoacid_mutations = self.__sequence_alterations()

            return aminoacid_mutations

        return []

    def __sequence_alterations(self):
        "Identifies the alterations present in the sequences."

        for specie, initial_pos in self.__initial_pos.items():
            return [
                self.__ref_aminoacid[position]
                + str(initial_pos + position)
                + self.__query_aminoacid[position]
                for position in range(len(self.__query_aminoacid))
                if self.__ref_aminoacid[position] != self.__query_aminoacid[position]
            ]

    def __is_equal(self, reference_sequence, query_sequence):
        "Verifies if two sequences are equals."

        return str(reference_sequence) == str(query_sequence)
