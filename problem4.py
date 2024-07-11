def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if n > len(lines):
                n = len(lines)
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'file.txt'  
n = 5  
read_last_n_lines(file_path, n)
