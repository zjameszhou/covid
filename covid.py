
# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

urlGlabalConfirmedCases = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

urlGlabalRecoveredCases = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
countries = ['date', 'US', 'Canada', 'France', 'India']

df = pd.read_csv(urlGlabalConfirmedCases).copy()

del df['Lat'], df['Long']


df = df.rename(columns={
    'Province/State': 'State',
    'Country/Region': 'Country'
}, inplace=False)


df = df.groupby(['Country'], as_index=True, group_keys=True).sum().T.rename_axis(
    'date').reset_index()

df = df[countries]

df['date'] = pd.to_datetime(df['date'], utc=True)

df.set_index('date', inplace=True)

df.to_csv(r'confirmed_global.csv')


# df = df.asfreq('b')

# df.isna().sum()

# df['United Kingdom'].diff().plot(figsize=(20,5), xlabel='date')
