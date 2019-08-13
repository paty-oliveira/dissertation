class AppExecutionError(Exception):
    def __init__(self):
        self.message = (
            "Error during the execution of the application. Please try again."
        )

    def __str__(self):
        return "{}".format(self.message)


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
