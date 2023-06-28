import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password123'
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE recipes")