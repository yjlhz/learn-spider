import requests

res = requests.get("http://www.taobao.com")
print(res.encoding)
print(res.headers)
# requests.post()
# requests.put()-+
# requests.options()
# requests.patch()
# requests.delete()