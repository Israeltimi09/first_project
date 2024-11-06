import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "092005",
    database = "classicmodels",
    port = 3306
)
if(connection.is_connected()):
    print("Connected to MySQL database")
else:
    print("DB could not be connected")