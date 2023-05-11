import sqlite3
from sqlite3 import Error

## Creating a database if one is not already present
## Also connecting the database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
         
            
cnn = None

##BEFORE YOU RUN THIS SCRIPT MAKE SURE THAT YOU SCROLL DOWN TO THE BOTTOM AND CHANGE THE FILEPATH
##THE FILEPATH HERE SHOULD MATCH THE FILEPATH DOWN THERE
filename =r"C:\Users\KianP\Desktop\Kian NEA\Database.db"

def createTableManInfo():
    try:
        with open('createmanagerinfo.sql', "r") as sql_command:
            sql = sql_command.read()
            
            cnn = sqlite3.connect(filename)
            print("Database connected")
            
            cs = cnn.cursor()
            cs.executescript(sql)
            cnn.commit()
            
            sql = 'SELECT * FROM managerInfo;'
            
            cs.execute(sql)
            records = cs.fetchall()
            
            for rec in records:
                print(rec)

    except Error as e:
        print(e)
    
    finally:
        if cnn:
            cnn.close()
            
def insertDataManInfo():
    
            
if __name__ == '__main__':
    ##CHANGE THE FILEPATH TO WHERE YOU WANT YOUR DATABASE TO BE CREATED AND WHAT TO NAME IT
    create_connection(r"C:\Users\KianP\Desktop\Kian NEA\Database.db")
    createTableManInfo()
    
            

 

