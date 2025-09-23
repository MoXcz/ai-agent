import os
from google.genai import types


def write_file(working_directory, file_path, content):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(cwd, file_path))

    if not full_path.startswith(cwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(full_path)):
        try:
            os.makedirs(os.path.dirname(full_path))
        except Exception as e:
            return f"Error: Cannot create directories: {e}"
    if os.path.isdir(full_path):
        return f"Error: It's a directory, expected a file"

    try:
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: cannot write contents to file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Wrtie content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path describes where in the path can the file be found, noting that the file must be inside the working directory to work.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content contains the content which will be written to the file in the current working directory.",
            ),
        },
    ),
)
