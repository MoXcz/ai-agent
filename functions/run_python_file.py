import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(cwd, file_path))

    if not full_path.startswith(cwd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    ext = os.path.splitext(full_path)[1]
    if ext != ".py":
        return f"Error: '{file_path}' is not a Python file."

    try:
        result = subprocess.run(
            ["python3", full_path] + args,
            timeout=30.0,
            capture_output=True,
            cwd=cwd,
            text=True,
        )

        out = ""
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if result.stdout:
            out += f"STDOUT:\n{result.stdout}\n"
        if result.stderr:
            out += f"STDERR:\n{result.stderr}"
        return out if out else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"
