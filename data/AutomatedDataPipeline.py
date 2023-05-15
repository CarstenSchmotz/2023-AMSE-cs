import pandas as pd

downloadFiles = True


#latitude,longitude,speed,shock_duration,shock_x_axis,x_axis,shock_y_axis,y_axis,shock_z_axis,z_axis,wagonID,delta_timestamp
if(downloadFiles):
    #df = pd.read_csv('https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_09.xlsx?__blob=publicationFile&v=4', sep=',', storage_options=storage_options, nrows=15, usecols=["latitude", "longitude", "speed"])
    df = pd.read_excel('https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_12.xlsx?__blob=publicationFile&v=4', sheet_name=4, usecols="B:P", skiprows=range(1,12))#header=[7,8,9,10,11]) #skiprows=[0,1,2,3,4,5,6,101,102]) 
# >>> pd.read_excel('tmp.xlsx', index_col=0, comment='#')  #try this
 #use col machen und header entfernen
else:
   df = pd.read_excel('/Users/carstenschmotz/Downloads/fz28_2022_09.xlsx', sheet_name=4,header=[7,8,9,10,11] )

df.columns.values[0] = 'Monat'
df.columns.values[1] = 'Insgesamt'
df.columns.values[2] = 'Alternative Antrieb'
df.columns.values[3] = 'Alternative in Prozent'
df.columns.values[4] = 'Elektroantriebe Ingesamt'
#df.columns.values[5] = ''

df.to_sql('carregistration', 'sqlite:///data/CarRegistration.sqlite', if_exists='replace', index=False)

print("First DONE ")

if(downloadFiles):
    df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/61243-0002_00.csv', sep=';', encoding="ISO-8859-1",skiprows =[0,1,2,3,4,5])
#usecols=['Strompreise für Haushalte: Deutschland', 'Jahre',
#'Jahresverbrauchsklassen', 'Preisbestandteile',
#'Durchschnittspreise für Strom und Gas'
#,'Deutschland'])
else:

    df = pd.read_csv('/Users/carstenschmotz/Downloads/61243-0002_00.csv', sep=';', skiprows=[0,1,2,3,4])


df.columns.values[0] = 'Jahr'
df.columns.values[1] = 'Verbrauchsklassen'
df.columns.values[2] = 'Energie und Vertrieb'
df.columns.values[1] = 'Haushalte'
df.columns.values[2] = 'Insgesamt'

df.to_sql('prize', 'sqlite:///data/Energyprize.sqlite', if_exists='replace', index=False)

print("Second DONE")