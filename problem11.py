import os

def get_file_size(file_path):
    try:
        file_size = os.path.getsize(file_path)
        return file_size
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = 'file.txt'  
file_size = get_file_size(file_path)
if file_size is not None:
    print(f"File size: {file_size} bytes")
