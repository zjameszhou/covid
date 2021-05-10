
# In[ ]:

import pandas as pd
from pandas import read_csv
from Data import *
import matplotlib.pyplot as plt


# In[ ]:


countries = ['Date', 'France', 'India']

urlGlabalConfirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
urlGlabalRecovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
urlGlabalDeaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


GlabalConfirmed = Data(urlGlabalConfirmed, countries, 'GlabalConfirmed.csv')
GlabalConfirmed.processData('Total_Confirmed_', 'Daily_Confirmed_')

GlabalRecovered = Data(urlGlabalRecovered, countries, 'GlabalRecovered.csv')
GlabalRecovered.processData('Total_Recovered_', 'Daily_Recovered_')

GlabalDeaths = Data(urlGlabalDeaths, countries, 'GlabalDeath.csv')
GlabalDeaths.processData('Total_Death_', 'Daily_Death_')

Data.merge()

# In[ ]:

confirmedT_cols = []
confirmedD_cols = []
deathT_cols = []
deathD_cols = []
recoveredT_cols = []
recoveredD_cols = []

c = countries.copy()

c.remove('Date')

for x in c:
    confirmedT_cols.append('Total_Confirmed_' + x)
    confirmedD_cols.append('Daily_Confirmed_' + x)
    deathD_cols.append('Daily_Death_' + x)
    deathT_cols.append('Total_Death_' + x)
    recoveredT_cols.append('Total_Recovered_' + x)
    recoveredD_cols.append('Daily_Recovered_' + x)

chartData = read_csv('Merged.csv', header=0,
                     parse_dates=[0], index_col=0)

# Chart for Total Deaths
chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Deaths',
    y=deathT_cols,
    title='Total Deaths'
).grid(color='gray', linewidth=0.3)

# Chart for Daily Deaths

chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Cases',
    y=deathD_cols,
    title='Daily Deaths'
).grid(color='gray', linewidth=0.3)

# Chart for Total Recovered
chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Recovered',
    y=recoveredT_cols,
    title='Total Recovered'
).grid(color='gray', linewidth=0.3)

# Chart for Daily Recovered

chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Recovered',
    y=recoveredD_cols,
    title='Daily Recovered'
).grid(color='gray', linewidth=0.3)


# Chart for Total Confirmed Cases
chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Confirmed',
    y=confirmedT_cols,
    fontsize=16,
    title='Total Confirmed'
).grid(color='gray', linewidth=0.3)

# Chart for Daily Recovered

chartData.plot(
    figsize=(20, 10),
    linewidth=1,
    xlabel='Date', ylabel='No. of Confirmed',
    y=confirmedD_cols,
    title='Daily Confirmed'
).grid(color='gray', linewidth=0.3)

df = read_csv('Merged.csv')


df['Date'] = df['Date'].apply(lambda a: pd.to_datetime(a).date())
df.to_excel('covid_data.xlsx', 'data')

writer = pd.ExcelWriter('covid_data.xlsx', engine='openpyxl', mode='a')
df.describe().to_excel(writer, 'summary')
df.tail(7).to_excel(writer, sheet_name='tail')


writer.save()
writer.close()
