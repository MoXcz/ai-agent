import os


def write_file(working_directory, file_path, content):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.join(cwd, file_path)

    if not os.path.abspath(full_path).startswith(cwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(full_path)):
        os.makedirs(os.path.dirname(full_path))

    with open(full_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
