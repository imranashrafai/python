print("======================== Post Request ========================")
import requests
from bs4 import BeautifulSoup

res = requests.get("https://uol.com")
print(res.text)


url = "https://priceoye.pk/wireless-earbuds/audionic/audionic-airbud-550"
r = requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

for anchors in soup.findAll("a"):
    print(anchors)
