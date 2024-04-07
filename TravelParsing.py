import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

url = requests.get("https://www.vl.ru/transport/search?from=Артем&to=Владивосток&day=&ts=0&te=24&route_number=&transport=train")  # отправка GET-запроса на сайт
html = BS(url.text, "lxml")
table = html.find("table")

headers = []
for i in table.find("thead").findAll("th")[1:-2]:
    title = i.text.replace("  ", "").replace("\n", "")
    headers.append(title)
print(headers)

mydata = pd.DataFrame(columns=headers)
for j in table.find("tbody").findAll("tr"):
    row_data = j.find_all("td")[1:-1]
    row = [i.text.replace("  ", "").replace("\n", "") for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row
print(mydata)
