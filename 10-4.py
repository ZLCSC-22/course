import requests
from bs4 import BeautifulSoup

url = f"https://books.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")  # 轉換成標籤樹

# 1
title = soup.title

# 2 尋找書的種類
code = soup.find("div", class_="side_categories")
# code = code.find_all("a") #這樣會把book也搜到，所以要改成以下
code = code.find("li").find("ul")
code = code.find_all("a")

category = []
for i in code:
  text = i.text
  text = text.replace("\n", "").replace(" ", "") #字串很亂，所以要處理
  category.append(text)

print(category)