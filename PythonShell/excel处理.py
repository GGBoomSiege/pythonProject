import pandas as pd
import os.path
import re

direct = os.getcwd() + "\\data\\"
file_lst = os.listdir(direct)
pattern = r"[1-9]{1}.xlsx"
columns_to_read = ['今日工作内容及进度']
writer = pd.ExcelWriter(direct + 'summary.xlsx', engine='xlsxwriter')  # 使用 xlsxwriter 作为引擎

num = 1
current_data_lst = []

for file in file_lst:
    if re.findall(pattern, file):
        data = pd.read_excel(direct + file, usecols=columns_to_read)
        for index,row in data.iterrows():
            content = row['今日工作内容及进度']
            old_data = re.sub('\.','、',content).replace(' ','').replace('\t','').replace('\n','').replace('\xa0','').strip()
            current_data = list(filter(None,re.split("\d+、",re.sub(r'\d+%','',old_data))))
            current_data_lst.append(current_data)
        cdata = pd.DataFrame(current_data_lst)
        cdata.to_excel(writer, sheet_name="Sheet" + str(num), index=False)
        current_data_lst = []

        num += 1

# 保存并关闭ExcelWriter对象
writer.book.close()  # 关闭xlsxwriter.Workbook对象
writer.close()
