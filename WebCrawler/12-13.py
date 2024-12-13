from bs4 import BeautifulSoup
import requests

keyword = input("請輸入搜尋關鍵字: ")

web = requests.get(f"https://www.zlsh.tp.edu.tw/category/news/?keyword={keyword}").text
soup = BeautifulSoup(web, "html.parser")
items = soup.select(".news_title")

for i in items:
    print(
        i.get_text()
        .replace("置頂", "")
        .replace("重要", "")
        .replace("轉知", "")
        .strip()
    )
