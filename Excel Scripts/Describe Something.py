import pandas as pd

df1= pd.read_csv('F:/Steve/enrollments.csv', encoding='latin1')
description= df1.describe()


description.to_csv('F:/Steve/PPEP F18 Average Score w 0s Described.csv', encoding='latin1')