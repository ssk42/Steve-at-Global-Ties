import pandas as pd 

# df1= pd.read_csv('F:/Steve/Completed PPEP F18 with SFID.csv', encoding='latin1')
# df2= pd.read_csv('F:/Steve/user_visits.csv', encoding='latin1', )
# df3= pd.read_csv('F:/Steve/PPEP F18 with SFID.csv', encoding='latin1')
# df_users= pd.read_csv('F:/Steve/users 122018.csv',encoding='latin1')
# df_ApE=pd.read_csv('F:/Steve/Attempts per Enrollment.csv', encoding='latin1',usecols=[7,31])
# df_Emails=pd.read_csv('F:/Steve/PPEP Analytics/Fall 2018/PPEP F18 All Analytics Pivot with SFID.csv', encoding='latin1')
df_AllwTime=pd.read_csv('F:/Steve/Attempts Per Enrollment with Time Spent.csv', encoding='latin1')
df_AllwSFID=pd.read_csv('F:/Steve/F18Fall Member IDs.csv', encoding='latin1', usecols=[3,4])


#df_attemptedEnrollments=pd.merge(df_enrollments,df_attempts,how ='inner',on='enrollment_id')
df_attemptedEnrollments2=pd.merge(df_AllwTime, df_AllwSFID, how='inner',on='Email')

df_attemptedEnrollments2.to_csv('F:/Steve/PPEP F18 Actually All Analytics.csv', encoding='latin1')




# result=pd.merge(df1,df2, how='inner')
# allResult=pd.merge(df3,df2, how='inner')

# print(result.describe())
# result.to_csv('F:/Steve/PPEP F18 Completed Analytics with SFID.csv', encoding='latin1')
# allResult.to_csv('F:/Steve/PPEP F18 All Analytics with SFID.csv', encoding='latin1')