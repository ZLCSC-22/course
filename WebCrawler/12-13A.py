import bs4, requests
map(lambda item: print(item.get_text().replace("置頂", "").replace("重要", "").replace("轉知", "").strip()), bs4.BeautifulSoup(requests.get(f"https://www.zlsh.tp.edu.tw/category/news/?keyword={input("請輸入搜尋關鍵字: ")}").text, "html.parser").select(".news_title"))
