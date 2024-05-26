# lib/file_io.py

def write_file(file_name, file_content):
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + '.txt'
    # Write the content to the file
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_file(file_name, file_content):
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + '.txt'
    # Append the content to the file
    with open(file_name_with_extension, 'a') as file:
        file.write(file_content)

def read_file(file_name):
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + '.txt'
    # Read and return the content of the file
    with open(file_name_with_extension, 'r') as file:
        return file.read()
