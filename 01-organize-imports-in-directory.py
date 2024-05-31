import os
import subprocess

def organize_imports_in_directory(directory):
    """
    Organize imports and remove unused imports in all Python files within the specified directory.

    :param directory: Path to the directory containing Python files
    """
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Remove unused imports using autoflake
                subprocess.run(['autoflake', '--in-place', '--remove-all-unused-imports', file_path])
                # Sort and organize imports using isort
                subprocess.run(['isort', file_path])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Reorganize and remove unused imports from Python modules in a folder.")
    parser.add_argument('directory', type=str, help='Path to the directory containing Python files.')

    args = parser.parse_args()
    organize_imports_in_directory(args.directory)
