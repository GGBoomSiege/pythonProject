import re

str = '3 室 2 厅 · 140㎡ · 南 · 中楼层/30层 · 精装'
lst = re.sub(r'\s+', '', str).split('·')
print(lst[0],'-'.join(lst[1:]))
