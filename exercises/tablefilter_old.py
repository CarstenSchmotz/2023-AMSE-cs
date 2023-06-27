import pandas as pd
import sqlite3
from sqlalchemy.types import Integer, FLOAT,String

carreg_table = "./CarRegistration.sqlite"
energy_table = "./Energyprize.sqlite"
print('find Path')
conn = sqlite3.connect(carreg_table)
print("works")

cursor = conn.cursor()
teilstring = 'Jahr'
sql_query = '''
SELECT * FROM carregistration
where Monat LIKE '%{}%' 
'''.format(teilstring)
df = pd.read_sql_query(sql_query, conn)
conn.close

Result = './Result.sqlite'
conn_neu = sqlite3.connect(Result)
df.to_sql('Cars',conn_neu, if_exists= 'replace', index= False)
print('Carfilter Done')
conn_neu.close
    
    
    
    


conn_reverse = sqlite3.connect(Result)


cursor = conn_reverse.cursor()

sql_query_reverse = '''
SELECT * FROM Cars
ORDER BY rowid DESC
'''
df = pd.read_sql_query(sql_query_reverse, conn_reverse)
df.to_sql('Cars',conn_reverse, if_exists= 'replace', index= False)


conn_reverse.close



#Remove text in columns















#Energy prizes
conn_reverse = sqlite3.connect(energy_table)


cursor = conn_reverse.cursor()

sql_query_reverse = '''
SELECT * FROM Prize
ORDER BY rowid DESC
'''
df = pd.read_sql_query(sql_query_reverse, conn_reverse)
df.to_sql('prize',conn_reverse, if_exists= 'replace', index= False)


conn_reverse.close


#filter only year prize
conn = sqlite3.connect(energy_table)

print("Energy Table Found")

cursor = conn.cursor()
sql_query = '''
SELECT * FROM prize
where Haushalte = 'Insgesamt' '''

df = pd.read_sql_query(sql_query, conn)
conn.close
#Result = './Result.sqlite'
conn_neu = sqlite3.connect(Result)
df.to_sql('Prize',conn_neu, if_exists= 'replace', index= False)
print('Energyfilter Done')
conn_neu.close






#def main():
 #   filter_car()
print('done')
   # filter_energy()


#if __name__ == " __main__":
 #   main()