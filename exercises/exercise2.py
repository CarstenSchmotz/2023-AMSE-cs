import pandas as pd
from sqlalchemy.types import String, Float, BigInteger

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
df = df[df['IFOPT'].str.match(r'^[a-z]{2}:\d+:\d+(:\d+)?(:\d+)?$',na=False)]

#Drop empty cells
df.dropna()


columnTypes = {'EVA_NR': BigInteger, 'DS100': String,'IFOPT': String,'NAME': String,'Verkehr': String ,'Laenge': Float,'Breite': Float,'Betreiber_Name': String }
#Write to sqlite
df.to_sql('trainstops', 'sqlite:///exercises/trainstops.sqlite', if_exists= 'replace', index=False)