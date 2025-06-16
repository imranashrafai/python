import os

files = os.listdir("OOP/os-module-prac")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"OOP/os-module-prac/{file}", f"OOP/os-module-prac/{i}.png")
        i += 1  # i=i+1
