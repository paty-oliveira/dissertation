import subprocess
import os
import urllib.request


def add_elements(first_element, second_element):
    "Add elements to a list."

    return list([first_element, second_element])


def convert_path(path):
    "Convert windows path format for linux format."

    cmd_args = ["wslpath", path]
    result = (
        subprocess.run(cmd_args, stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .replace("\n", "")
    )
    return str(result)


def download(url, file_name, path):
    "Executes the download of the file from specific URL."

    try:
        filepath = os.path.join(path, file_name)
        urllib.request.urlretrieve(url, filepath)

    except ConnectionRefusedError as error:
        return error


def execution_status(code, execution_codes):
    "Verify the status of the code inserted based on execution codes."
    
    for status, message in execution_codes.items():
        if status == code:
            return message


def preffix(string, number):
    "Returns the first characters of the string."

    return string[0 : int(number)]


def suffix(string, number):
    "Returns the last characters of the string."

    return string[-int(number) :]


def valid_file(file):
    "Checks if the valid isn't empty."

    return os.path.getsize(file)


def valid_path(path):
    "Checks if the path is valid."

    return os.path.exists(path)


def valid_string(list_strings, valid_characters):
    "Checks if string has the correct characters."

    return all(
        character in valid_characters for string in list_strings for character in string
    )
