import os
from collections import Counter

def count_lines(file_path):
    """
    Count the number of non-empty lines in a file.

    Args:
    - file_path (str): Path to the file.

    Returns:
    - int: Number of non-empty lines.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return len(lines)

def generate_report(workspace_path):
    """
    Generate a report for a given workspace.

    Args:
    - workspace_path (str): Path to the workspace.

    Prints:
    - Various metrics about the workspace.
    """
    # Define the file extensions for popular programming languages
    file_extensions = ['.py', '.java', '.js', '.cpp', '.c', '.html', '.css', '.php']  # Add more as needed

    folder_count = 0
    file_count = 0
    max_depth = 0
    total_lines_of_code = 0
    max_lines_file = ('', 0)

    # Traverse through the workspace using os.walk
    for root, dirs, files in os.walk(workspace_path):
        folder_count += len(dirs)
        file_count += len(files)

        # Calculate the depth of the current folder in the workspace
        depth = root[len(workspace_path):].count(os.sep)
        max_depth = max(max_depth, depth)

        # Iterate through files in the current folder
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1]

            # Check if the file has a valid programming language extension
            if file_extension in file_extensions:
                # Count lines of code and update metrics
                lines_of_code = count_lines(file_path)
                total_lines_of_code += lines_of_code

                # Update the file with the highest line number
                if lines_of_code > max_lines_file[1]:
                    max_lines_file = (file_path, lines_of_code)

    # Print the generated report
    print(f"Number of folders: {folder_count}")
    print(f"Number of files: {file_count}")
    print(f"Maximum folder depth: {max_depth}")
    print(f"Total lines of code: {total_lines_of_code}")
    print(f"File with the highest line number: {max_lines_file[0]} ({max_lines_file[1]} lines)")

if __name__ == "__main__":
    # Input the path to the workspace or folder
    # Made the working directory the default path
    workspace_path = os.getcwd()
    generate_report(workspace_path)
