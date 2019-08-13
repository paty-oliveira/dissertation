class WrongOptionError(Exception):
    pass


class FileReadindError(Exception):
    pass


class ProcessExecutionError(Exception):
    pass


class WrongFilePath(WrongOptionError):
    def __init__(self):
        self.message = "Invalid file path. Please introduce a valid path."

    def __str__(self):
        return "{}".format(self.message)


class WrongSpecieError(WrongOptionError):
    def __init__(self):
        self.message = "Error in the specie syntax. Please introduce a valid specie."

    def __str__(self):
        return "{}".format(self.message)


class WrongGeneError(WrongOptionError):
    def __init__(self):
        self.message = "Error in the gene syntax.Please introduce a valid gene."

    def __str__(self):
        return "{}".format(self.message)


class WrongPrimerError(WrongOptionError):
    def __init__(self):
        self.message = "Error in the primer syntax. Please introduce a valid primer."

    def __str__(self):
        return "{}".format(self.message)


class EmptyFileError(FileReadindError):
    def __init__(self):
        self.message = "Empty file. Please introduce new file."

    def __str__(self):
        return "{}".format(self.message)


class InvalidFileError(FileReadindError):
    def __init__(self):
        self.message = "The file extension isn´t supported. Please introduce a correct file."

    def __str__(self):
        return "{}".format(self.message)


class SpecieIdentificationError(ProcessExecutionError):
    def __init__(self):
        self.message = "Error during the specie identification."
    
    def __str__(self):
        return "{}".format(self.message)


class AntifungalResistanceProcessError(Exception):
    def  __init__(self):
        self.message = "Error during the detection of antifungal resistance."

    def __str__(self):
        return "{}".format(self.message)


class InformationExtractionError(Exception):
    def  __init__(self):
        self.message = "Error during the information extraction."

    def __str__(self):
        return "{}".format(self.message)


class SequenceLengthError(Exception):
    def __init__(self):
        self.message = "The sequence introduced haven't a correct length. Please review the sequence."

    def __str__(self):
        return "{}".format(self.message)


class PipitsExecutionError(Exception):
    def __init__(self):
        self.message = "An error has occurred during the PIPITS process."

    def __str__(self):
        return "{}".format(self.message)