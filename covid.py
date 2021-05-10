
# In[ ]:

import pandas as pd
from pandas import read_csv
from Data import *


# In[ ]:


startDate = '2021-01'
endDate = '2021-05'
cols_plot = ['Daily_Confirmed_US',
             'Daily_Confirmed_France', 'Daily_Confirmed_India']


urlGlabalConfirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
urlGlabalRecovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
urlGlabalDeaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

countries = ['Date', 'France', 'India']


GlabalConfirmed = Data(urlGlabalConfirmed, countries, 'GlabalConfirmed.csv')
GlabalConfirmed.processData('Total_Confirmed_', 'Daily_Confirmed_')

GlabalRecovered = Data(urlGlabalRecovered, countries, 'GlabalRecovered.csv')
GlabalRecovered.processData('Total_Recovered_', 'Daily_Recovered_')

GlabalDeaths = Data(urlGlabalDeaths, countries, 'GlabalDeath.csv')
GlabalDeaths.processData('Total_Death_', 'Daily_Death_')

Data.merge()

# In[ ]:
df = read_csv('Merged.csv', header=0,
              parse_dates=[0], index_col=0)

df.plot(
    figsize=(20, 10),
    linewidth=0.8,
    marker='.',
    xlabel='Date', ylabel='No. of cases',
    y=cols_plot,
    title='Glabal Daily Confirmed Cases'
).grid(color='gray', linewidth=0.3)

# df.loc[startDate:endDate].plot(
#     figsize=(20, 10),
#     linewidth=0.8,
#     marker='.',
#     xlabel='Date', ylabel='No. of cases',
#     y=cols_plot,
#     title='Glabal Daily Confirmed Cases'
# ).grid(color='gray', linewidth=0.3)
