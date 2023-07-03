import pandas as pd
import urllib.request
import zipfile 


#Download zip file
urllib.request.urlretrieve("https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip", "./exercises/exercise4.zip")

#Extract zip file
zip = zipfile.ZipFile("./exercises/exercise4.zip")
zip.extractall('./exercises')


#Read csv file
df = pd.read_csv("./exercises/data.csv",sep=';', decimal=',', index_col=False, 
                 usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])

#Rename the columns
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

#Transfomr temperatur
df['Temperatur']= df['Temperatur'] * 9/5 +32 
df['Batterietemperatur']=df['Batterietemperatur'] * 9/5 +32

#Validate data
df = df[(df["Geraet"] > 0) & 
        (df["Monat"] > 0) ]
     
#Write to sqlite
df.to_sql('temperatures', 'sqlite:///temperatures.sqlite', if_exists= 'replace', index=False)
