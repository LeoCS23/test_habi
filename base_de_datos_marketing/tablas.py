import mysql.connector

#creamos la conexción a la base de datos
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "marketingBebidas"
)

cursor = conn.cursor()

#Ejecutamos en la base de datos la tabla que queremos crear
sql = """CREATE TABLE TIENDA(
    codigo_tienda INT,
    nombre_tienda VARCHAR(255),
    PRIMARY KEY (codigo_tienda)
    )"""
cursor.execute(sql)

sql = """CREATE TABLE BEBIDA(
    codigo_bebida INT,
    nombre_bebida VARCHAR(255),
    PRIMARY KEY (codigo_bebida)
    )"""
cursor.execute(sql)

sql = """CREATE TABLE BEBEDOR(
    cedula BIGINT,
    nombre VARCHAR(255),
    PRIMARY KEY (cedula)
    )"""
cursor.execute(sql)

sql = """CREATE TABLE VENDE(
    codigo_tienda INT,
    codigo_bebida INT,
    precio FLOAT,
    FOREIGN KEY (codigo_tienda) REFERENCES TIENDA (codigo_tienda),
    FOREIGN KEY (codigo_bebida) REFERENCES BEBIDA (codigo_bebida)
    )"""
cursor.execute(sql)

sql = """CREATE TABLE FRECUENTA(
    cedula BIGINT,
    codigo_tienda INT,
    PRIMARY KEY (cedula),
    FOREIGN KEY (codigo_tienda) REFERENCES TIENDA (codigo_tienda)
    )"""
cursor.execute(sql)

sql = """CREATE TABLE GUSTA(
    cedula BIGINT,
    codigo_bebida INT,
    PRIMARY KEY (cedula),
    FOREIGN KEY (codigo_bebida) REFERENCES BEBIDA (codigo_bebida)
    )"""
cursor.execute(sql)

conn.commit()

cursor.execute("SHOW TABLES")

for dato in cursor:
    print(dato)


conn.close()