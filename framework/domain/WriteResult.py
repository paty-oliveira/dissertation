import os


class WriteResult:

    """
        It allows the writing of the results.
    """

    def __init__(self, results_path):
        self.__path = results_path

    # def write_identification(self, results):
    #     "Writes a report with the result of PIPITS identification process in a *.txt file."

    #     head = "Identification of fungi species:\nNumber\tKindgom\tPhylo\tClass\tOrder\t Family\t Genus\t Specie\t\n"

    #     with open(
    #         os.path.join(self.__path, "specie_identification.txt"), "w"
    #     ) as output_file:
    #         output_file.write(head)
    #         output_file.write(results)

    def write(self, results):
        "Writes a report with the results of the all mutations detected in a *.txt file."

        with open(
            os.path.join(self.__path, "mutations_result.csv"), "w"
        ) as output_file:
            header = "Reference, Position, Substitutions"
            to_write = "\n".join(
                "{}, {}, {}".format(str(x[0]), str(x[1]), str(x[2])) for x in results
            )
            output_file.write(header)
            output_file.write(to_write)

        return output_file
