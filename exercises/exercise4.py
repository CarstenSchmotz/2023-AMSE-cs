import pandas as pd
import numpy as np
import urllib.request
import zipfile as ZipFile



df = urllib.request.urlretrieve("https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip", 'zipfile')

#zipresp = urlopen(zipurl)
    # Create a new file on the hard drive
tempzip = open("/tmp/tempfile.zip", "wb")
    # Write the contents of the downloaded file into the new file
tempzip.write(df.read())
    # Close the newly-created file
tempzip.close()
    # Re-open the newly-created file with ZipFile()
zf = ZipFile("/tmp/tempfile.zip")
    # Extract its contents into <extraction_path>
    # note that extractall will automatically create the path
zf.extractall(path = '///.exercises/')
    # close the ZipFile instance
zf.close()
'''#Download csv File
df = pd.read_csv("data.csv",sep=';', decimal=',')

#Drop Status column
df = df.drop(['Status'], axis=1)

#Then, drop all rows with invalid values in Verkehr:
df = df[df['Verkehr'].isin(['FV','RV','nur DPN'])]

#>= or > is enough
df = df[(df['Temperatur'] * 9/5 +32 )& ((df['Betterietemperatur'] * 9/5 +32 ) ]

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
df.to_sql('temperatures', 'sqlite:///temperatures.sqlite', if_exists= 'replace', index=False)
'''