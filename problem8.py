def find_longest_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest_length = len(max(words, key=len))
            longest_words = [word for word in words if len(word) == longest_length]
        return longest_words
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'file.txt' 
longest_words = find_longest_words(file_path)
print("Longest words:", longest_words)
