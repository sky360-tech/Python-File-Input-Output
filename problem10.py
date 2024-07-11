from collections import Counter
import re

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  
            words = re.findall(r'\b\w+\b', text)  
            word_counts = Counter(words)  
        return word_counts
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

file_path = 'file.txt'  
word_frequency = count_word_frequency(file_path)
for word, count in word_frequency.items():
    print(f"{word}: {count}")
