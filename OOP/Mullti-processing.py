# print("======================== Multi Processing ========================")
import requests
import os
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP")

if not os.path.exists("files"):
    os.mkdir("files")


def downloadFile(url, name):
    print(f"Starting Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Ending Downloading {name}")


pros = []

url = "https://picsum.photos/2000/3000"
if __name__ == "__main__":
    for i in range(11, 17):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()


# concurrent future using map function
if __name__ == "__main__":
    with ProcessPoolExecutor() as ppe:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        results = ppe.map(downloadFile, l1, l2)
        # Printing output of function ike if function returns value then it will ive value otherwise return NONE
        for r in results:
            print(r)
