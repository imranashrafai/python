print("======================== Generators ========================")
import os


# these functions generate values on the fly or run time not need to store and very efficient in memory management
def py_gen():
    for i in range(8):
        yield i


p = py_gen()
# print(next(p))
for i in p:
    print(i)


def log_file_reader(filename):
    os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP")
    try:
        with open(filename, "r") as file:
            for line in file:
                # strip removes space from the beginig of line and at the end of line
                yield line.strip()
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Usage:
log_lines = log_file_reader("test.txt")

for line in log_lines:
    # Process each log line one by one without loading the entire file into memory
    print(line)
