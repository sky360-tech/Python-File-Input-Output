def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List has been written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'file.txt'  
data_list = ['apple', 'banana', 'cherry', 'date']
write_list_to_file(file_path, data_list)
