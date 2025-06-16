print("======================== AsyncIO ========================")
import os
import asyncio
import requests

os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP")
try:
    os.mkdir("downloadedByASYNCIO")
except Exception:
    print("Directory already found")


async def function1():
    os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP\downloadedByASYNCIO")
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("img3.jpg", "wb").write(response.content)


async def function2():
    os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP\downloadedByASYNCIO")

    print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("img2.jpg", "wb").write(response.content)


async def function3():
    os.chdir("D:\IMRAN ASHRAF\BS-IT\Python\Learning Stage\OOP\downloadedByASYNCIO")

    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("img.jpg", "wb").write(response.content)


async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)


asyncio.run(main())
