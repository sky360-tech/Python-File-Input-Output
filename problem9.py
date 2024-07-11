def count_lines_in_file(file_path):
    line_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return line_count


file_path = 'file.txt'  
number_of_lines = count_lines_in_file(file_path)
print(f"Number of lines in the file: {number_of_lines}")
