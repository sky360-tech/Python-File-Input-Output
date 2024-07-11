def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = '\\100.101.70.33\files3\Python Problems\Python File Input Output\file.txt' 
read_file(file_path)
