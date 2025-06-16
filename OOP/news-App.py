print("======================== News App ========================")
import requests
import json


newstype = input("Enter the type of news!")
url = f"https://newsapi.org/v2/everything?q={newstype}&from=2023-08-13&sortBy=publishedAt&apiKey=6e59b73b331845138f70b365a83a3c8e"
r = requests.get(url)

news = json.loads(r.text)
for articles in news["articles"]:
    print(articles["title"])
    print(articles["description"])
    print("------------------------------------------------------")
