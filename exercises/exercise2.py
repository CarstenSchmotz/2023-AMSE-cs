import pandas as pd
import numpy as np


#Download csv File
df = pd.read_csv("https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV",sep=';', decimal=',')

#Drop Status column
df = df.drop(['Status'], axis=1)

#Then, drop all rows with invalid values in Verkehr:
df = df[df['Verkehr'].isin(['FV','RV','nur DPN'])]

#>= or > is enough
df = df[(df['Laenge']>= -90 )& (df['Laenge']<= 90) & (df['Breite']>= -90 )& (df['Breite']<= 90) ]

#Valid "IFOPT" values follow this pattern:
#<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
df = df[df['IFOPT'].str.contains(r'^[A-Za-z]{2}:\d*:\d*(?::\d*)?$',na=False)]

#Change empty cells to nan
df.replace('',np.nan, inplace=True)

#Drop nan cells
df.dropna(inplace=True)

#Convert column 'Betreiber_Nr' to integer
df['Betreiber_Nr'] = df['Betreiber_Nr'].astype(int)

#Write to sqlite
df.to_sql('trainstops', 'sqlite:///trainstops.sqlite', if_exists= 'replace', index=False)