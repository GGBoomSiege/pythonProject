# DATA_DICT = {
#     '1': {'name': '张三', 'age': 18},
#     '2': {'name': '李四', 'age': 18},
#     '3': {'name': '王五', 'age': 18},
#     '4': {'name': '赵六', 'age': 18}
# }
#
# for item in DATA_DICT.items():
#     print(item)

import re
string = '计算机软件已上市1000-9999人'
tmp = '-'.join(re.findall(r'\d+',string))
print(type(tmp))