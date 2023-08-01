import re

text = "、"
pattern = re.compile(r'[\u4e00-\u9fff、，。！？]+')

result = pattern.findall(text)

print(result)