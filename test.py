import requests
r = requests.get("https://gank.io/api/v2/data/category/{}/type/{}/page/1/count/10".format('GanHuo','app'))
print(r.json())