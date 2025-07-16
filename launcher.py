import path

def open_file_by_extention(filepath):
    file_extension = path.extname(filepath)
    try:
        if file_extension == '.txt':
            with open(filepath, 'r') as f:
                content = f.read()
                print(f"Content of text file '{filepath}':\n{content}")
        elif file_extension == '.csv':
            with open(filepath, 'r') as f:
                lines = f.readlines()
                print(f"Content of CSV file '{filepath}':")
                for line in lines:
                    print(line.strip())
        elif file_extension == '.log':
            with open(filepath, 'r') as f:
                content = f.read()
                print(f"Content of log file '{filepath}':\n{content}")
        elif file_extension == '.py':
            with open(filepath, 'r') as f:
                content = f.read()
                print(f"Content of Python script '{filepath}':\n{content}")
        else:
            print(f"Unsupported file type: '{file_extension}'. Cannot open automatically.")
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
    except Exception as e:
        print(f"An error occurred while opening '{filepath}': {e}")


location = r"C:\Users\ltbx\Downloads\exercises.csv"
open_file_by_extention(location)