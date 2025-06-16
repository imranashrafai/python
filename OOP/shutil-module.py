print("======================== Shutil Module ========================")
import shutil
import os

# copy the whole folder with its subdirectories and files
try:
    shutil.copytree("D:/IMRAN ASHRAF/BS-IT/Python", "D:/Mypython")
    print("Folder copied successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# copy the file with eta tags(when file created,time, created by etc)
try:
    shutil.copy2("OOP/class-methods.py", "D:/class-methods.py")
    print("File copied successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    os.remove("D:/class-methods.py")
    print("Folder deleted successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


try:
    shutil.rmtree("D:/Mypython")
    print("Folder deleted successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
