import pandas as pd
import openpyxl
import numpy

##This is the SurveyGizmo export. This is the master data.
hotelDF= pd.read_csv('F:/Steve/hotels.csv', encoding='latin1')

## These identify the proper columns from the original hotel spreadsheet.
blackout= hotelDF.columns[hotelDF.columns.str.startswith('Blackout')]
oneIVLP= hotelDF.columns[hotelDF.columns.str.startswith('Hotel can accommodate ONE (1)')]
twoIVLP= hotelDF.columns[hotelDF.columns.str.startswith('Hotel CAN accommodate two (2)')]
hotelNamesDF= pd.DataFrame(hotelDF['Hotel Name'])


## The following section makes the newly found columns into dataFrames. It starts with Blackout dates, then One IVLP Group, then Two IVLP Groups
hotelBlackoutDF= hotelDF[blackout]
hotelBlackoutDF= pd.merge(hotelNamesDF,hotelBlackoutDF, on=hotelBlackoutDF.index)
# hotelBlackoutDF.to_csv('F:/Steve/testBlackoutHotels.csv')
hotelOneDF= hotelDF[oneIVLP]
hotelOneDF= pd.merge(hotelNamesDF,hotelOneDF, on=hotelOneDF.index)
# hotelOneDF.to_csv('F:/Steve/testOneHotels.csv')
hotelTwoDF= hotelDF[twoIVLP]
hotelTwoDF= pd.merge(hotelNamesDF,hotelTwoDF, on=hotelTwoDF.index)
# hotelTwoDF.to_csv('F:/Steve/testTwoHotels.csv')

def hotelName(num):
	if num==0:
		return 'Embassy Row Hotel'
	if num==1:
		return 'Hampton Inn DC Convention Center'
	if num==2:
		return 'The Churchill Hotel'
	if num==3:
		return 'The Darcy'
	if num==4:
		return 'Residence Inn Washington DC Downtown'
	if num==5:
		return 'Homewood Suites by Hilton, Downtown'
	if num==6:
		return 'Washington Marriott Georgetown'
	if num==7:
		return 'ONE WASHINGTON CIRCLE HOTEL'
	if num==8:
		return 'The Fairfax At Embassy Row'
	if num==9:
		return 'Washington Plaza Hotel'
	if num==10:
		return 'Kimpton Hotel Palomar'
	if num==11:
		return 'Kimpton Carlyle Hotel'
	if num==12:
		return 'The Donovan'
	if num==13:
		return 'Washington Hilton'
	if num==14:
		return 'Club Quarters Washington DC'
	if num==15:
		return 'Melrose'

## The following section starts the main gist of the program. The first part sets up the dictionary entries per unique IVLP date range.
dateRangesDF= pd.read_csv('F:/Steve/Hotel Date Ranges.csv')
dateRangesDF= pd.DataFrame(dateRangesDF['Check-In'])
for dateName,dateRangeRow in dateRangesDF.iteritems():
	for name, values in hotelBlackoutDF.iteritems():
		dateDict={}
		for x in range(0, 16):
			# print(x, values[x])
			if(values[x]=='Blackout dates'):
				dateDict[x]=hotelName(x)
				#test
				# print(dateRangeRow)
	print(dateDict[16])
				# print(numpy.linspace(values[x],15))



