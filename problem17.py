def remove_newlines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line.strip() + ' ')
        
        print(f"Newlines removed and content updated in {file_path}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'file.txt' 
remove_newlines(file_path)
