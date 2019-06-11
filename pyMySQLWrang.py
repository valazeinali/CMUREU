import pymysql as db

HOST = "192.168.64.2"
PORT = 3306
USER = "local"
PASSWORD = "local" # Username for this is local & so is password
DB = "CMU"

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB) # create database connecition
try:
    dbhandler = connection.cursor() # create a cursor object
    dbhandler.execute("select * from Issue_Num_Label;") # exceute the query
    result = dbhandler.fetchall() # fetch all data from the cursor area
    for item in result:  # result is a two dimensional array now, print using two loops.
        for it in item:
            print (it, " ",)
        print ("\n")

except Exception as e:
    print (e)

finally:
    connection.close()