
# In[ ]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Data:

    def __init__(self, url, countries, fileName):
        self.url = url
        self.countries = countries
        self.fileName = fileName

    def processData(self):

        df = pd.read_csv(self.url).copy()

        del df['Lat'], df['Long']

        df = df.groupby(['Country/Region'], as_index=True, group_keys=True).sum().T.rename_axis(
            'Date').reset_index()
        df['Date'] = pd.to_datetime(df['Date'], utc=True)

        df = df[self.countries]

        df.set_index("Date", inplace=True)

        df.to_csv(self.fileName)


urlGlabalConfirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
urlGlabalRecovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
urlGlabalDeaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

countries = ['Date', 'US', 'Canada', 'France', 'India']

GlabalConfirmed = Data(urlGlabalConfirmed, countries, 'GlabalConfirmed.csv')
GlabalConfirmed.processData()

GlabalRecovered = Data(urlGlabalRecovered, countries, 'GlabalRecovered.csv')
GlabalRecovered.processData()

GlabalDeaths = Data(urlGlabalDeaths, countries, 'GlabalDeaths.csv')
GlabalDeaths.processData()

# df = df.asfreq('b')

# df.isna().sum()

# df['United Kingdom'].diff().plot(figsize=(20,5), xlabel='date')
