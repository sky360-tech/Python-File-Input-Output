def read_file_to_variable(file_path):
    content = ""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content


file_path = 'file.txt' 
file_content = read_file_to_variable(file_path)
print(file_content)
