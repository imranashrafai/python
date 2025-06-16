print("========================OS Module========================")

import os

# make folder if not exist in current folder
if not os.path.exists("osPractice"):
    os.mkdir("osPractice")
# make 100 floders in that folder which is i made recently "osPractice"
for i in range(0, 100):
    os.mkdir(f"ospractice/osToutorial{i+1}")
# rename the folders
for i in range(0, 100):
    # rename(source(path of current folder name),destination(path to rename folder))
    os.rename(f"ospractice/osToutorial{i+1}", f"ospractice/osTout {i+1}")

folders = os.listdir("osPractice")
print(folders)
# to print folders and files in folders
for fold in folders:
    print(fold)
    print(os.listdir(f"osPractice/{fold}"))


# To know in wchich directory we are operating
print(os.getcwd())

# To Change directory
print(os.chdir(".vscode/"))

print(os.getcwd())
