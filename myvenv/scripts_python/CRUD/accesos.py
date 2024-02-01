import mysql.connector
from mysql.connector import Error

def crear_conexion():
    conexion = mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "D95102918526a*",
        database = "tienda_online")
        

print("Conexión Exitosa")
crear_conexion()