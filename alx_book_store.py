import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Do!mybest2121",
    database="Do!mybest2121"
)

print(mydb.get_server_info())