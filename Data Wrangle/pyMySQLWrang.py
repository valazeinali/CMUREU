import pymysql as db

HOST = "192.168.64.2"
PORT = 3306
USER = "local"
PASSWORD = "local" # Username for this is local & so is password
DB = "CMU"

labels = {
'A-NLL',
'A-allocators',
'A-async-await',
'A-attributes',
'A-build',
'A-codegen',
'A-const-fn',
'A-diagnostics',
'A-edition-2018-lints',
'A-iterators',
'A-lifetimes',
'A-lint',
'A-macros',
'A-macros-1.2',
'A-mir',
'A-rust-2018-preview',
'A-rustbuild',
'A-stability',
'A-traits',
'A-unicode',
'T-compiler',
'T-core',
'T-dev-tools',
'T-dev-tools-rustdoc',
'T-doc',
'T-infra',
'T-lang',
'T-libs',
'T-release',
'T-rustdoc'
} #python dictionary, storing possible values of labels 

label = [] #python list

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB) # create database connecition
try:
    dbhandler = connection.cursor() # create a cursor object
    dbhandler1 = connection.cursor()
    dbhandler.execute("SELECT * from Issue_Num_Label;") # exceute the query
    dbhandler1.execute("SELECT * from PR_Ref;")
    result = dbhandler.fetchall() # fetch all data from the cursor area
    result1 = dbhandler1.fetchall()

    #for item in result:
    	#for it in item:
    		#temp = result.fetch(str(Issue_Num_Label.labels))
     
    for item in result:  # result is a two dimensional array now, print using two loops.
        for it in item:
            print (it, " ",)
        print ("\n")
    for item1 in result1:  # result is a two dimensional array now, print using two loops.
        for it1 in item1:
            print (it1, " ",)
        print ("\n")

except Exception as e:
    print (e)

finally:
    connection.close()
    