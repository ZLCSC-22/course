import requests
from bs4 import BeautifulSoup

url = f"https://books.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")  # 轉換成標籤樹

# 1 (取得每本書的li - 上節課教的)
code = soup.find("div", class_="col-sm-8 col-md-9")
code = code.find("section").find("ol")

# 3（新的方法 - 使用select方法）
code = soup.select_one("section").select_one(".row").select("li")

# 2 (超級簡單的方式 - select的一行解)
code = soup.select(".col-xs-6.col-sm-4.col-md-3.col-lg-3")

# 處理每個li裡面的資料
for i in code:
  book_name = i.find("h3").find("a").get("title")
  book_price = i.find("p", class_="price_color").text
  print(f"{book_name}\n{book_price}")
  print("-------------")

# print(code)