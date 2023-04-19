import pandas as pd

file = './data/1.xlsx'

data = pd.read_excel(file)
data.loc[:,'C'] = data.apply(lambda x: 1 if x['A'] > (x['B']*0.5) else 0,axis=1)
print(data)