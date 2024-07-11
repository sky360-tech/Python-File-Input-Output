def combine_files(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
            for line1, line2 in zip(file1, file2):
                combined_line = f"{line1.strip()} {line2.strip()}\n"
                output_file.write(combined_line)
        print(f"Combined lines have been written to {output_file_path}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file1_path = 'file.txt'  
file2_path = 'file1.txt'  
output_file_path = 'combined_output.txt'  
combine_files(file1_path, file2_path, output_file_path)
