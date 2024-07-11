def create_alphabet_file(file_path, letters_per_line, include_lowercase=False):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Uppercase letters
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'  # Lowercase letters
    alphabet = alphabet_upper + (alphabet_lower if include_lowercase else '')
    num_letters = len(alphabet)
    
    try:
        with open(file_path, 'w') as file:
            for i in range(0, num_letters, letters_per_line):
                line = alphabet[i:i + letters_per_line]
                file.write(line + '\n')  
        print(f"File '{file_path}' created with {letters_per_line} letters per line.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'alphabet_full.txt'  
letters_per_line = 5  
include_lowercase = True 
create_alphabet_file(file_path, letters_per_line, include_lowercase)
