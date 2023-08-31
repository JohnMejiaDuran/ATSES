import mysql.connector

def conexionBD():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        db='atses'
    )
    if mydb: 
        print("Conexion exitosa")
    else: 
        print("Error de conexión")
    return mydb