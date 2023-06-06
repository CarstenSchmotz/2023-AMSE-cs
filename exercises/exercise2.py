import pandas as pd

#Download csv File
df = pd.read_csv("https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV",sep=';', decimal=',')

#Drop Status column
df = df.drop(['Status'], axis=1)

#Then, drop all rows with invalid values in Verkehr:
df = df[df['Verkehr'].isin(['FV','RV','nur DPN'])]


df = df[(df['Laenge']> -90 )& (df['Laenge']< 90)]
#Drop empty cells
df.dropna()
#Write to sqlite
df.to_sql('trainstops', 'sqlite:///exercises/trainstops.sqlite', if_exists= 'replace', index=False)