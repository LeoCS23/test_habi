#Creamos la base de datos

import mysql.connector #Libreria para conectar la base de datos

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE marketingBebidas")
cursor.execute("SHOW DATABASES")
#conn.commit()


for dato in cursor:
    print(dato)


conn.close()