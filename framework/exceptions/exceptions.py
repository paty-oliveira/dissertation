class WrongFilePath(Exception):
    def __init__(self):
        self.message = "Invalid file path. Please introduce a valid path."

    def __str__(self):
        return "{}".format(self.message)


class WrongSpecieError(Exception):
    def __init__(self):
        self.message = "Error in the specie syntax. Please introduce a valid specie."

    def __str__(self):
        return "{}".format(self.message)


class WrongGeneError(Exception):
    def __init__(self):
        self.message = "Error in the gene syntax.Please introduce a valid gene."

    def __str__(self):
        return "{}".format(self.message)


class WrongPrimerError(Exception):
    def __init__(self):
        self.message = "Error in the primer syntax. Please introduce a valid primer."

    def __str__(self):
        return "{}".format(self.message)


class EmptyFileError(Exception):
    def __init__(self):
        self.message = "Empty file. Please introduce new file."

    def __str__(self):
        return "{}".format(self.message)


class InformationExtractionError(Exception):
    def __init__(self):
        self.message = "Error during the information extraction."

    def __str__(self):
        return "{}".format(self.message)


class InvalidSequenceError(Exception):
    def __init__(self):
        self.message = "The sequence isn't valid. Please review the sequence."

    def __str__(self):
        return "{}".format(self.message)


class InvalidTranslationError(Exception):
    def __init__(self):
        self.message = "The amino acid sequence haven't a valid length. Please review the sequence."

    def __str__(self):
        return "{}".format(self.message)


class PipitsExecutionError(Exception):
    def __init__(self):
        self.message = "An error has occurred during the PIPITS process."

    def __str__(self):
        return "{}".format(self.message)
