def is_file_closed(file):
    return file.closed


file_path = 'file.txt'  

try:
    with open(file_path, 'r') as file:
        print(f"File closed status (inside 'with' block): {is_file_closed(file)}")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"File closed status (outside 'with' block): {is_file_closed(file)}")
