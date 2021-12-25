import re

info = "姓名:yjlhz 生日:1999年6月2日 本科:2018年9月7日"

print(re.findall("\d{4}",info))
print(re.match(".*生日.*\d{4}",info))