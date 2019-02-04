import pandas as pd 

df1= pd.read_csv('F:/Steve/Master Roster.csv', encoding='latin1')
df1['Email']=df1['Email'].str.lower()
df2= pd.read_csv('F:/Steve/PPEP F18 All Analytics Pivot with SFID.csv', encoding='latin1', )
df2['Email']=df2['Email'].str.lower()

result=pd.merge(df1,df2, how='outer')

result.to_csv('F:/Steve/PPEP F18 All Analytics as Outer with SFID.csv', encoding='latin1')
