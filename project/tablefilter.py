import pandas as pd
import sqlite3
from sqlalchemy.types import Integer, FLOAT,String

carreg_table = "./CarRegistration.sqlite"
energy_table = "./Energyprize.sqlite"






#Car registrations
conn_reverse = sqlite3.connect(carreg_table)
cursor = conn_reverse.cursor()

#Reverse data to match
sql_query_reverse = '''
SELECT * FROM carregistration
ORDER BY rowid DESC
'''
df = pd.read_sql_query(sql_query_reverse, conn_reverse)
df.to_sql('carregistration',conn_reverse, if_exists= 'replace', index= False)
conn_reverse.close





conn = sqlite3.connect(carreg_table)
cursor = conn.cursor()

#Filter the sums of the years
teilstring = 'Jahr'
sql_query = '''
SELECT * FROM carregistration
where Monat LIKE '%{}%' 
'''.format(teilstring)
df = pd.read_sql_query(sql_query, conn)
conn.close

Result = './data.sqlite'
conn_neu = sqlite3.connect(Result)
df.to_sql('Cars',conn_neu, if_exists= 'replace', index= False)
conn_neu.close

print('Carfilter done')   
    
    
    






#Energy prizes
conn_prize = sqlite3.connect(energy_table)
cursor = conn_prize.cursor()

#Reverse data to match
sql_query_reverse = '''
SELECT * FROM Prize
ORDER BY rowid DESC
'''
df = pd.read_sql_query(sql_query_reverse, conn_prize)
df.to_sql('prize',conn_prize, if_exists= 'replace', index= False)
conn_prize.close



conn = sqlite3.connect(energy_table)
cursor = conn.cursor()

#Filter the sums of the years
sql_query = '''
SELECT * FROM prize
where Haushalte = 'Insgesamt' '''

df = pd.read_sql_query(sql_query, conn)
conn.close

conn_neu = sqlite3.connect(Result)
df.to_sql('Prize',conn_neu, if_exists= 'replace', index= False)
conn_neu.close

print('Energyfilter done')





