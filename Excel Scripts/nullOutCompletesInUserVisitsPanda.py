import pandas as pd 
from pandas.io.json import json_normalize


df1 = pd.read_csv('F:/Steve/user_visits.csv')
df2= pd.read_csv('F:/Steve/wbusers.csv')
df3= pd.read_csv('F:/Steve/Finished participants Fall 2018.csv',usecols=[4])
df4= pd.read_csv('F:/Steve/Master Roster.csv',usecols=[0], encoding="latin1")

result= pd.merge(df1,df2[['user_id','email']],on='user_id')

CompletedResult=pd.merge(left=result, right=df3, how="inner")
LoggedInResult=pd.merge(left=result, right=df4, how="inner", on='email')

LoggedInResult=pd.read_csv('F:/Steve/Logged In Participants Pivot.csv')

LoggedInResult.describe().to_csv('F:/Steve/Logged In Participants Results.csv')
#print(CompletedResult.describe())
CompletedResult.to_csv('F:/Steve/Completed Participants.csv')
result.to_csv('F:/Steve/All Par')
# LoggedInResult.to_csv('F:/Steve/Logged In Participants.csv')



# ResultOfPivotTable= pd.read_csv('F:/Steve/Describe PPEP Fall 2018.csv')
# Some= ResultOfPivotTable.describe()
# print(Some)
# Some.to_csv('F:/Steve/Description of PPEP Fall 2018 Results.csv')

# df1= pd.read_csv('F:/Steve/JSON.csv',usecols=[3])
# describe= df1
# try:
# 	describe=json_normalize(df1)
# except AttributeError:
# 	pass
# describe.to_excel('F:/Steve/Test of Completed Users.xlsx',sheet_name='Bleh')

##
##
##ws1 = wb1.active
##bridgeUsersWS = wb2.active
##finishersWS= wb3.active
##from openpyxl.utils import range_boundaries
##min_col, min_row, max_col, max_row = range_boundaries('A1:H')
##
###This looks at colunn B
##column= 2
##counter=0
###test
##
####TODO:
###Convert to Email
###Check Email is Complete
###If not, Make Email=0
##
##
##
##for userVisits in ws1.iter_rows():
##        if userVisits[column].value!=2:
##                for rowNum in range(len(bridgeUsersWS['A'])):
##                    if userVisits[column].value== bridgeUsersWS['A'][rowNum].value:
##                        userVisits[column].value=bridgeUsersWS['B'][rowNum].value
##                        counter=counter+1
####                for finisher in range(len(finishersWS['E'])):
####                    if userVisits[column].value== finishersWS['E'][finisher].value.lower():
####                        userVisits[column].value=finishersWS['C'][finisher].value.lower()                        
###                       counter=counter+1
####                        #test
##                        
##                        print("appending..."+str(counter))
##
##wb1.save("F:/Steve/testingFile.xlsx")
