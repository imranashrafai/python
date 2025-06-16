import os

os.chdir("D:/")
print(os.getcwd())

folders = os.listdir("D:/IMRAN ASHRAF")
pathofFol="D:/IMRAN ASHRAF"
print(folders)
if os.path.exists("D:/IMRAN ASHRAF"):
    for fold in folders:
        print(fold)
os.rename(f"{pathofFol}/contacts.csv", f"{pathofFol}/cont.csv")
