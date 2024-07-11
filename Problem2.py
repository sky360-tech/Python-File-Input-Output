def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for i in range(n):
                line = file.readline()
                if line:
                    print(line.strip())
                else:
                    break
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = '\\100.101.70.33\files3\Python Problems\Python File Input Output\file.txt'  
n = 5  
read_first_n_lines(file_path, n)
