import os

def delete_temporary_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Temporary file '{file_path}' deleted successfully.")
    else:
        print(f"File '{file_path}' does not exist.")

# Example usage:
temp_file_path = "path/to/temporary/file.txt"
delete_temporary_file(temp_file_path)