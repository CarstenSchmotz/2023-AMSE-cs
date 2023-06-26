import pandas as pd
import sqlite3
from sqlalchemy.types import Integer, FLOAT,String

carreg_table = "./CarRegistration.sqlite"
energy_table = "./Energyprize.sqlite"

#columtypes float and string
def filter_car(tablename):
    con = sqlite3.connect(carreg_table)
    
    return

def filter_energy(tablename):
    con = sqlite3.connect(energy_table)
    
    



def main():
    filter_car()
    filter_energy()


if __name__ == " __main__":
    main()