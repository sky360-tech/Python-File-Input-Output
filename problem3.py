def append_text_to_file(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')
        print(f"Appended text: {text_to_append}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content after appending:")
            print(content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'file.txt'  
text_to_append = 'Hi'  

append_text_to_file(file_path, text_to_append)
read_file(file_path)
