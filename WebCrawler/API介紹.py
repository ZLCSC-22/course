import requests
import json

# 0. 什麼是JSON? https://www.oracle.com/tw/database/what-is-json/

# 1.笑話API https://jokeapi.dev/
res = requests.get("https://v2.jokeapi.dev/joke/Any").text
res_json = json.loads(res)
# question = res["setup"]

print(res_json)