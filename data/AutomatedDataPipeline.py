import pandas as pd

downloadFiles = False

storage_options = {'User-Agent': 'Mozilla/5.0'}

#latitude,longitude,speed,shock_duration,shock_x_axis,x_axis,shock_y_axis,y_axis,shock_z_axis,z_axis,wagonID,delta_timestamp
#if(downloadFiles):
    #df = pd.read_csv('https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_09.xlsx?__blob=publicationFile&v=4', sep=',', storage_options=storage_options, nrows=15, usecols=["latitude", "longitude", "speed"])
 #   df = pd.read_excel('https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_09.xlsx?__blob=publicationFile&v=4', index_col=None, header=None) 
#else:
 #   df = pd.read_csv('C:/Users/nicol/Downloads/ShockData.csv', sep=',', nrows=15, usecols=["latitude", "longitude", "speed"])

#df.columns.values[0] = 'lat'
#df.columns.values[1] = 'lon'
#df.columns.values[2] = 'speed2'

#df.to_sql('carregistration', 'sqlite:///2023-amse-nb/data/CarRegistration.sqlite', if_exists='replace', index=False)

#print("First DONE ")

if(downloadFiles):
    df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/61243-0002_00.csv', sep=';')
else:
    df = pd.read_csv('C:/Users/Besitzer/Downloads/61243-0002_00.csv', sep=';',nrows=20)
print('test')
df.to_sql('prize', 'sqlite:///2023-amse-cs/data/Energyprize.sqlite', if_exists='replace', index=False)

print("Second DONE")