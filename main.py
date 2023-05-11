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
        ##with statement means will only run if script is accessable
        with open('createmanagerinfo.sql', "r") as sql_command:
            ##reading the sql file
            sql = sql_command.read()
            
            ##connecting the database so that changes can be made
            conn = sqlite3.connect(filename)
            print("Database connected")
            
            ##cursor is needed to create/modify/insert in a database
            cursor = conn.cursor()
            ##running sql file
            cursor.executescript(sql)
            ##commiting changes to the database
            conn.commit()
            
            ##fetching all added records so that they can be printed for debug
            records = cursor.fetchall()
            
            ##printing records for debug
            for rec in records:
                print(rec)

    ##throws an error in case database file is not found
    ##or if SQL script you want to fun is not found or has bad syntax
    except Error as e:
        print(e)
    
    ##Closes the database again after use because it is good practice
    finally:
        if conn:
            conn.close()
            
            
def insertDataManInfo():
    try:
        ##connecting the database and creating a cursor
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        
        ##simple bool for the use of confirming email
        emailGood = False
        
        member_ID = input("Enter your uniqe employee ID: ")
        
        ##asking for inputs of data
        name = input("Enter full name: ")
        
        ##while loop so user can confirm email
        while not emailGood:
            emailOne = input("Enter email address: ")
            emailTwo = input("Confirm email address: ")
            if emailOne == emailTwo:
                emailGood = True
            else:
                print("Email adressed do not match")
        
        hourRate = float(input("Input your hourly rate: "))
        
        ##Inserting the inputs into the database
        cursor.execute("INSTERT INTO managerInfo(member_ID, name, email, hourRate) VALUES (?,?,?,?)")
        ##Comitting the changes
        conn.commit()
        print("New data inserted")
        
    
    except Error as e:
        print(e)
    
    finally:
        if conn:
            conn.close()
    
            
if __name__ == '__main__':
    ##CHANGE THE FILEPATH TO WHERE YOU WANT YOUR DATABASE TO BE CREATED AND WHAT TO NAME IT
    create_connection(r"C:\Users\KianP\Desktop\Kian NEA\Database.db")
    createTableManInfo()
    insertDataManInfo()
    
            

 

