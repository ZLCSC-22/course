from bs4 import BeautifulSoup
import requests

#   本日教課流程
# 1. 複習上節課的HTTP
# 2. 用瀏覽器查看學校網站原始碼
# 3. 解釋為什麼原始碼沒有出現公告的文字
# 3. 介紹Python Request模組
# 4. 用GET取得學校原始碼
# 5. 看學校的「行政公告」原始碼  https://www.zlsh.tp.edu.tw/category/news/news_01/

web = requests.get("https://www.zlsh.tp.edu.tw/category/news/news_01/").text
soup = BeautifulSoup(web, "html.parser")  # 轉換成標籤樹
sticky = soup.select(".sticky")

for i in sticky:
  print(i.select_one(".news_title").get_text().replace('置頂', '').replace('重要', '').strip())