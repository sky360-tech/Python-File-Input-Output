def extract_characters_from_files(file_paths):
    characters = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                characters.extend(content)  # Add characters to the list
        except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred with file {file_path}: {e}")
    return characters


file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  
characters_list = extract_characters_from_files(file_paths)

print(f"Extracted {len(characters_list)} characters.")
print("Characters:", characters_list)
