import pandas as pd 

df1= pd.read_csv('F:/Steve/Fall 2018 PPEP with Result.csv', encoding='latin1')
df2= pd.read_csv('F:/Steve/users 122018.csv', encoding='latin1', )
df3= pd.read_csv('F:/Steve/program_enrollments.csv', encoding='latin1')

result=pd.merge(df2,df3, on='user_id', how='inner')
CompletedResult= pd.merge(df1,result, on='Email', how="inner")



CompletedResult.to_csv('F:/Steve/PPEP F18 with SFID.csv', encoding='latin1')