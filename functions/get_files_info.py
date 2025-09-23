import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.join(cwd, directory)

    if not os.path.abspath(full_path).startswith(cwd):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    if not os.path.isdir(full_path):
        return f"Error: '{directory}' is not a directory"

    files = os.listdir(full_path)
    return_string = ""

    for file in files:
        filepath = os.path.join(full_path, file)
        return_string += f"- {filepath}: file_size={os.path.getsize(filepath)}, is_dir={os.path.isdir(filepath)}\n"
    return return_string


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
