import re
str = input("zifuchuan")
num = re.findall(r"\d+\.?\d+",str)
print(num[0].rstrip("0"))