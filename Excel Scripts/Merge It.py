import pandas as pd 

primaryLocation='F:/Steve/'
secondaryLocation='C:/users/sreitz/Downloads/'

location=primaryLocation
fileName='November 2018 Mexico PPEP Mexico Training Institute'

# df1= pd.read_csv('F:/Steve/Completed PPEP F18 with SFID.csv', encoding='latin1')
# df2= pd.read_csv('F:/Steve/user_visits.csv', encoding='latin1', )
df_contactSFID= pd.read_csv('F:/Steve/PPEP F18 with SFID.csv', encoding='latin1', usecols=[2,3,4,5,8])
df_contactSFID['Email']=df_contactSFID['Email'].str.lower()
# df_users= pd.read_csv('F:/Steve/users 122018.csv',encoding='latin1')
# df_ApE=pd.read_csv('F:/Steve/Attempts per Enrollment.csv', encoding='latin1',usecols=[7,31])
# df_Emails=pd.read_csv('F:/Steve/PPEP Analytics/Fall 2018/PPEP F18 All Analytics Pivot with SFID.csv', encoding='latin1')
# df_AllwTime=pd.read_csv('F:/Steve/Attempts Per Enrollment with Time Spent.csv', encoding='latin1')
# df_AllwSFID=pd.read_csv('F:/Steve/F18Fall Member IDs.csv', encoding='latin1', usecols=[3,4])
df_toMerge= pd.read_csv('C:/users/sreitz/Downloads/Salesforce csv/Nov 2018 MTI.csv', encoding='latin1')
df_toMerge['Email']=df_toMerge['Email'].str.lower()

#df_attemptedEnrollments=pd.merge(df_enrollments,df_attempts,how ='inner',on='enrollment_id')
#df_attemptedEnrollments2=pd.merge(df_AllwTime, df_AllwSFID, how='inner',on='Email')
df_mergeIt=pd.merge(df_contactSFID, df_toMerge, how='right', on='Email')

df_mergeIt.to_csv(location+fileName+'.csv', encoding='latin1')




# result=pd.merge(df1,df2, how='inner')
# allResult=pd.merge(df3,df2, how='inner')

# print(result.describe())
# result.to_csv('F:/Steve/PPEP F18 Completed Analytics with SFID.csv', encoding='latin1')
# allResult.to_csv('F:/Steve/PPEP F18 All Analytics with SFID.csv', encoding='latin1')