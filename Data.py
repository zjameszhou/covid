
# In[ ]:
import pandas as pd


class Data:

    def __init__(self, url, countries, fileName):
        self.url = url
        self.countries = countries.copy()
        self.fileName = fileName

    def processData(self, totalPreFix, dailyPreFix):

        df = pd.read_csv(self.url).copy()

        df.to_csv('raw_' + self.fileName)
        print('Saved: raw_' + self.fileName)

        del df['Lat'], df['Long']

        df = df.groupby(['Country/Region'], as_index=True, group_keys=True).sum().T.rename_axis(
            'Date').reset_index()
        df['Date'] = pd.to_datetime(df['Date'], utc=True)

        df = df[self.countries]

        df.set_index("Date", inplace=True)

        if len(self.countries) == 0:
            print('list is empty')
        else:
            self.countries.remove('Date')

        for x in self.countries:
            df[totalPreFix + x] = df[x]
            df[dailyPreFix + x] = df[x] - df[x].shift().fillna(0)
            del df[x]

        df.to_csv(self.fileName)

        print('Saved: ' + self.fileName)

    def merge():
        f1 = pd.read_csv('GlabalConfirmed.csv', index_col=[0])
        f2 = pd.read_csv('GlabalDeath.csv', index_col=[0])
        f3 = pd.read_csv('GlabalRecovered.csv', index_col=[0])

        pd.concat([f1, f2, f3], axis=1).to_csv('Merged.csv')
        print('Saved: Merged.csv')
