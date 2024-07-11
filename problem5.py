def read_file_to_list(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]  # Remove leading/trailing whitespace
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


file_path = 'file.txt'  
lines = read_file_to_list(file_path)
print(lines)
