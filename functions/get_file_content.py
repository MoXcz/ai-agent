import os
from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.join(cwd, file_path)

    if not os.path.abspath(full_path).startswith(cwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read() != "":
                file_content += (
                    f'...File "{file_path}" truncated at {MAX_CHARS} characters.'
                )

            return file_content
    except Exception as e:
        return f"Error: Could not read file {file_path}\n{e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content inside a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path describes where in the path can the file be found, noting that the file must be inside the working directory to work.",
            ),
        },
    ),
)
