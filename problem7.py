def read_file_to_array(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip()) 
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


file_path = 'file.txt' 
lines_array = read_file_to_array(file_path)
print(lines_array)
