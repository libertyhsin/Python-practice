from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
page = 55
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "?SrtT=rt"
    print("處理url:", url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("Finish")
        break
    html = BeautifulSoup(response)
    # print(html.find_all("li", class_="list-rst"))
    # find:找到第一個符合條件
    # find_all:找所有符合條件 return list
    # print(html.find_all("li", {"class": "list-rst js-list-item"}))
    for r in html.find_all("li", class_="list-rst js-list-item"):
        ja_name = r.find("small", class_="list-rst__name-ja")
        en_name = r.find("a", class_="list-rst__name-main")
        score = r.find("b", class_="c-rating__val")
        price = r.find_all("span", class_="c-rating__val")
        # 萃取紙條.text 萃取特別特徵([特徵])
        print(ja_name.text, en_name.text, score.text, price[0].text, price[1].text, en_name["href"])
    page += 1
