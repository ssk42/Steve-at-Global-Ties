import pandas as pd

df1= pd.read_csv('F:/Steve/CPG Amount.csv', encoding='latin1')
df1=df1['FY2017 CPG Total']
description= df1.describe()

# print(description)
description.to_csv('F:/Steve/fy17 Described.csv', encoding='latin1')