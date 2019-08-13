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
    pass


class InvalidFileError(FileReadindError):
    pass


class SpecieIdentificationError(ProcessExecutionError):
    pass


class ResistanceDetectionError(ProcessExecutionError):
    pass


class InformationExtractionError(Exception):
    pass


class SequenceLengthError(Exception):
    pass

    
class PipitsExecutionError(Exception):
    pass
