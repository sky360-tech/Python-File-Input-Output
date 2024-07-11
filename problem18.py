def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        return word_count
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'file.txt'  
word_count = count_words_in_file(file_path)
if word_count is not None:
    print(f"The number of words in the file is: {word_count}")
else:
    print("Unable to count words.")
