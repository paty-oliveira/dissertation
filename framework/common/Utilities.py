import subprocess

def execution_status(code, execution_codes):
    for status, message in execution_codes.items():
        if status == code:
            return message

def convert_path(path):
    "Convert windows path format for linux format."

    cmd_args = ["wslpath", path]
    result = (
        subprocess.run(cmd_args, stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .replace("\n", "")
    )
    return str(result)
