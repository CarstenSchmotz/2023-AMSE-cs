import pandas as pd
import sqlite3
from sqlalchemy.types import Integer, FLOAT,String

carreg_table = "./CarRegistration.sqlite"
print('find Path')
energy_table = "./Energyprize.sqlite"

#columtypes float and string
#def filter_car():
conn = sqlite3.connect(carreg_table)
#df = pd.read_sql_query(sql="SELECT * FROM carregistration", con=con)
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
    #cursor.execute(sql_query)
    #df.to_sql(tablename, 'sqlite:///./result.sqlite', if_exists='replace', index=False)
    #con.commit()
    #con.close()
    

#def filter_energy(tablename):
 #   con = sqlite3.connect(energy_table)
    
    

#Energy prizes
conn = sqlite3.connect(energy_table)
#df = pd.read_sql_query(sql="SELECT * FROM carregistration", con=con)
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