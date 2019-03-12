import pandas as pd
import openpyxl
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

