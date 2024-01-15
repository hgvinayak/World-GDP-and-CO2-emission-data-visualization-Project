# PROJECT 2: VISUALIZATION OF WORLD GDP AND CARBON - DIOXIDE EMISSION
'''
The World Development Indicators dataset obtained from the World Bank containing over a thousand annual
indicators of economic development from hundreds of countries around the world.
'''

# Initial Exploration of the dataset
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cbook
import zipfile
import bz2
import warnings
import seaborn as sns
warnings.filterwarnings("ignore",category=matplotlib.MatplotlibDeprecationWarning)
# Let us read the dataset
data = pd.read_csv('D:\Data Sets\ML Projects Data\8 Advance Project Dataset\data\indicators.bz2')
#print(data)

# data.to_csv("D:\GDPandCo2.csv",index=False)

'''
        CountryName CountryCode  ...  Year         Value
0        Arab World         ARB  ...  1960  1.335609e+02
1        Arab World         ARB  ...  1960  8.779760e+01
'''
# Why we are using the "Warnings" library here  - warnings.filterwarnings("ignore",category=matplotlib.MatplotlibDeprecationWarning)
'''
The warning about deprecation in this context is related to features or behaviors within the Matplotlib library itself, not directly tied to your dataset. 
When you see a deprecation warning from Matplotlib, it means that the way you are using certain Matplotlib functions or features is considered obsolete, and those features might be changed or removed in future versions of Matplotlib.
'''

# Why bz2
'''
As now our data set is a csv format but compressed using "BZ2" compression algorithm. as it is a huge dataset that's why we converted it into bz2 format
'''

# Why ZIP
'''
If we are working with ZIP file then this library will help us to extrac the data
'''

# why cbook
'''
cbook is a module within Matplotlib that provides utilities for Matplotlib's internals.
It's used in the code to filter out deprecation warnings related to Matplotlib.
'''
print("shape of the data",data.shape)  # shape of the data (5656458, 6)
print("No of columns is given by",data.columns)
# ['CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year','Value']
'''
#From the above dataset, it looks like it has different indicators for different countries with the year and value of the indicator.
'''
# How many unique countries are there
countries = data['CountryName'].unique().tolist()
print("No of countries: ",len(countries)) # 247 unique contries
# How many country codes are there - it should be same as no of countries
country_codes = data['CountryCode'].unique().tolist()
print("No of country_codes: ",len(country_codes)) # 247
# how may indicators are there many or few
# How many unique indicators are there
indicators = data['IndicatorName'].unique().tolist()
print("No of indicators: ",len(indicators))
# How many years of data we have
years = data['Year'].unique().tolist()
print("No of years: ",len(years))
#what is the range of years
print(data['Year'].min(), "to",data['Year'].max())

# Data Visualization
# So here we have data related to each country (diffrent indicators) over the years , but this has huge data
# So now we want to analyze the data for one country and explore the CO2 emissions over the years
# For this we have 2 columns mainly " Indicator Name" - and "Country" , our data should be with the rows containing "CO2 emissions(metric per capita)" and USA
# So will take the intersection of these 2 masks

'''
Let us pick a country and an indicator to explore CO2 Emissions per capita 
and the USA.
To select CO2 emissions for the United States, We will take the intersection of two masks, one with all the rows that contains the string,
"C02 emissions" and the other which contains all the rows containing the string, "USA".
'''
# Here Basically we are filtering the 2 columns
# from "Indicator Name" - which contains the string "CO2 emissions (metric tons per capita)"
# from "Country" - which contains the string "

hist_indicator = 'CO2 emissions \(metric'
hist_country = 'Australia'
mask1 = data['CountryName'].str.contains(hist_country) # Filtering the Column "CountryName" which contains "USA"
#print("mask 1: India data------checking \n",mask1)
mask2 = data['IndicatorName'].str.contains(hist_indicator) # Filtering the Column "IndicatorName" which contains "CO2 emissions (metric tons per capita)"
#print("mask 2: CO2  data------checking \n",mask2)
stage = data[mask1 & mask2] # only data which contains both strings
#print("Checking-------",stage)
#  stage dataset contain indicators matching the USA for country code & CO2 emissions over time.
#print(stage.shape)
#print(stage.head())

# Lets see the CO2 value over the years how it is
years = stage['Year'].values
co2 = stage['Value'].values
# plot the histogram
#plt.plot(years,co2)
#plt.title("Line plot of Co2 values over the years")
#plt.ylabel("Co2 values")
#plt.xlabel("Year")
#plt.axis([1959,2011,0,25])
#plt.show()
#plt.bar(years,co2)
#plt.show()

# Okay let's see the only Co2 values
hist_data = stage['Value'].values
#print(len(hist_data))
#plt.hist(hist_data,bins=10,density=False,facecolor='green')
#plt.show()
#plt.boxplot(hist_data)
#plt.show()

# so in the year 2008 - almost the co2 emission value is reached to 17.86 , so will take the same year for all other country and see
# again we need to create the mask from the data
indicator = 'CO2 emissions \(metric'
year_ = 2008
mask3 = data['IndicatorName'].str.contains(indicator)
mask4 = data['Year'].isin([year_])
stage1 = data[mask3 & mask4]
print(stage1)

#country = stage1['CountryName']
#co2_value = stage1['Value'].values
#plt.bar(country,co2_value)
#plt.show()

print(len(mask4)) # 5656458

# Now for the Australia, will see the "Air transport, passengers carried" data

hist_indicator = 'Air transport carried'
hist_country = 'Australia'
mask5 = data['CountryName'].str.contains(hist_country) # Filtering the Column "CountryName" which contains "Austraia"
# #print("mask 5: India data------checking \n",mask5)
mask6 = data['IndicatorName'].str.contains(hist_indicator) # Filtering the Column "IndicatorName" which contains "Air passangers"
# #print("mask 6: CO2  data------checking \n",mask6)
stage3 = data[mask5 & mask6] # only data which contains both strings as we done the CO2 emission per capita for ausrtralia, will see the " Air transport, passengers carried"
print(stage3.head())

year = stage3['Year'].values
passangers = stage3['IndicatorName'].values
plt.plot(year,passangers)
plt.show()

