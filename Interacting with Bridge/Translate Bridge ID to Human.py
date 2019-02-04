import pandas as pd 


##Edit this to change the file name.
csvName='M1245 Course Visits with Emails'

df1= pd.read_csv('F:/Steve/M1245 Course Visits.csv', encoding='latin1')
#df1['Email']=df1['Email'].str.lower()
df2= pd.read_csv('F:/Steve/users 122018.csv', encoding='latin1', usecols=[0,2,6,7] )
#df2['Email']=df2['Email'].str.lower()

result=pd.merge(df1,df2, how='inner', on='user_id')

result.to_csv('F:/Steve/'+csvName+'.csv', encoding='latin1')
