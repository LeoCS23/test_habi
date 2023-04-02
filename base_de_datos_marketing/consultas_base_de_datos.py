import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "marketingBebidas"
)

# Creamos un cursor para realizar la consulta
cursor = conn.cursor()

#Consultar los bebedores que no les gusta la colombiana
cursor.execute("SELECT nombre FROM bebedor JOIN gusta ON bebedor.cedula = gusta.cedula WHERE gusta.codigo_bebida NOT IN (SELECT gusta.codigo_bebida FROM gusta JOIN bebida ON gusta.codigo_bebida = bebida.codigo_bebida WHERE bebida.nombre_bebida = 'colombiana')")


results = cursor.fetchall() # Recuperar los resultados de la consulta


for result in results: # Imprimir los resultados
  print(result)

#Consultar las fuentes de soda que no son frecuentadas por andres camilo restrepo
cursor.execute("SELECT nombre_tienda FROM tienda WHERE codigo_tienda NOT IN (SELECT codigo_tienda FROM frecuenta JOIN bebedor ON frecuenta.cedula = bebedor.cedula WHERE bebedor.nombre = 'Andres Camilo Restrepo')")

results = cursor.fetchall()

for result in results:
  print(result)

#Consultar los bebedores que les gusta al menos una bebida y que frecuentan al menos una tienda
cursor.execute("SELECT nombre FROM bebedor JOIN frecuenta ON bebedor.cedula = frecuenta.cedula WHERE bebedor.cedula IN (SELECT bebedor.cedula FROM bebedor JOIN frecuenta ON bebedor.cedula = frecuenta.cedula)")

results = cursor.fetchall()

for result in results:
  print(result)


#Consultar para cada bebedor, las bebidas que no les gustan
cursor.execute("SELECT nombre, bebida.nombre_bebida FROM bebedor JOIN gusta ON bebedor.cedula = gusta.cedula JOIN bebida ON gusta.codigo_bebida = bebida.codigo_bebida WHERE bebedor.cedula NOT IN (SELECT bebedor.cedula FROM bebedor JOIN gusta ON bebedor.cedula = gusta.cedula)")

results = cursor.fetchall()

for result in results:
  print(result)
  
#Consultar Los bebedores que frecuentan las tiendas que frecuenta Luis Perez
cursor.execute("SELECT nombre FROM bebedor JOIN frecuenta ON bebedor.cedula = frecuenta.cedula WHERE frecuenta.codigo_tienda IN (SELECT codigo_tienda FROM frecuenta JOIN bebedor ON frecuenta.cedula = bebedor.cedula WHERE bebedor.nombre = 'Luis Perez') AND bebedor.nombre <> 'Luis Perez'")

results = cursor.fetchall()

for result in results:
  print(result)

#Consultar Los bebedores que unicamente frecuentan las tiendas que unicamente sirven alguna bebida que le gusta.
cursor.execute("SELECT nombre FROM bebedor JOIN frecuenta ON bebedor.cedula = frecuenta.cedula JOIN tienda ON frecuenta.codigo_tienda = tienda.codigo_tienda JOIN vende ON tienda.codigo_tienda = vende.codigo_tienda JOIN bebida ON vende.codigo_bebida = bebida.codigo_bebida JOIN gusta ON bebida.codigo_bebida = gusta.codigo_bebida WHERE gusta.cedula IN (SELECT gusta.cedula FROM gusta JOIN bebedor ON gusta.cedula = bebedor.cedula)")

results = cursor.fetchall()

for result in results:
  print(result)

# Cerramos la conexión con la base de datos
cursor.close()
conn.close()