import sqlite3
from sqlite3 import Error


cnn = None
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
            

 

