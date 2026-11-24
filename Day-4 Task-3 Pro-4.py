def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


# Example usage
result = read_file_safely("test.txt")
print(result)