import requests
# import json

url = "https://www.base64decode.org/"
# r = requests.get(url=url)
# # data = r.json()
# 

r = requests.get(url)
print(r.status_code)
data = r.json()

