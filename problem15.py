import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                return None
            random_line = random.choice(lines).strip()
            return random_line
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = 'file.txt'  
random_line = read_random_line(file_path)
if random_line is not None:
    print(f"Random line: {random_line}")
else:
    print("The file is empty or an error occurred.")
