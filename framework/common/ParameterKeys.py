class ParameterKeys:
    FILEPATH_IDENTIFICATION = "filepath_identification"
    FILEPATH_DETECTION = "filepath_detection_mutation"
    IDENTIFICATION_KEY = "candida_identification"
    MUTATION_KEY = "detection_mutation"
    SPECIE_NAME = "specie_name"
    GENE_NAME = "gene_name"
    FORWARD_PRIMER = "forward_primer"
    REVERSE_PRIMER = "reverse_primer"

class ExecutionCode:
    ID_SUCCESS = "ID-1"
    ID_FAILED = "ID-0"
    ANTI_SUCCESS = "ANTI-1"
    ANTI_FAILED = "ANTI-0"

    message = {
        "ID-1" : "Specie identification was executed with sucess. Please check the results.",
        "ID-0" : "It wasn't possible execute the specie identification.",
        "ANTI-1" : "Antifungal resistance detection was executed with sucess. Please check the results.",
        "ANTI-0" : "Is wasn't possible execute the detection of antifungal resistance."
    }
        