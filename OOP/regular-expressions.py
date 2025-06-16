print("======================== Regular Expressions ========================")
import re

pattern = r"[a-z]a"
text = """Main article: List of flyovers in Pakistan

Nagan Chowrangi Flyover, Karachi
Many flyovers and underpasses are located in major urban areas of the country to segregate the flow of traffic. The highest number of flyovers and under passes are located in Karachi, followed by Lahore.[399] Other cities having flyovers and underpasses for the regulation of flow of traffic includes Islamabad-Rawalpindi, Faisalabad, Gujranwala, Multan, Peshawar, Hyderabad, Quetta, Sargodha, Bahawalpur, Sukkur, Larkana, Rahim Yar Khan and Sahiwal etc.[400]

Beijing Underpass, Lahore is the longest underpass of Pakistan with a length of about 1.3 km (0.81 mi).[401] Muslim Town Flyover, Lahore is the longest flyover of the country with a length of about 2.6 km (1.6 mi)"""

# mat=re.search(pattern,text)
matchall = re.finditer(pattern, text)
for words in matchall:
    print(words)
