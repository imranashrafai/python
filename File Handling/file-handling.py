print("========================File Handling========================")
# to write data in file
f = open("File Handling/myfile.txt", "w")
f.write("Hello! I am trying to learn File Handling concept in Python")
f.close()

# to read data from file
rf = open("File Handling/myfile.txt", "r")
fileReading = rf.read()
print(fileReading)
rf.close()

# if do not want to close file manually then use it:(appending data)
with open("File Handling/myfile.txt", "a") as ap:
    ap.write("\nI am appending data using shortcut method")

# writing the lines of list
with open("File Handling/myfile.txt", "w") as wrtL:
    lines = ["line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n", "line 6\n"]
    wrtL.writelines(lines)


# read data line by line
with open("File Handling/myfile.txt", "r") as reL:
    lines = reL.readlines()

for li in lines:
    print(li.strip())


with open("File Handling/myfile.txt", "r") as ia:
    # start to read data from 12th character
    ia.seek(12)
    read = ia.read(22)
    print(read)
    # tells current position of the file cursor
    print(ia.tell())


with open("File Handling/sam.txt", "w") as re:
    re.write("Hello World!")
    # it will store only 4 characters in our file
    re.truncate(4)

with open("File Handling/sam.txt", "r") as re:
    print(re.read())

