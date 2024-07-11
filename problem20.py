def generate_text_files():
    for i in range(26):
        letter = chr(65 + i)  # 65 is the ASCII value for 'A'
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the file named {file_name}")
        print(f"Created file: {file_name}")

generate_text_files()
