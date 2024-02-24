import pandas as pd
import snowflake.connector
import os 
import csv

def conectar_snowflake():
    """Función para conectar a Snowflake"""
    conn = snowflake.connector.connect(
        user=os.environ['SNOWSQL_USER'],
        password=os.environ['SNOWSQL_PWD'],
        account=os.environ['SNOWSQL_ACCOUNT'],
        warehouse='COMPUTE_WH',
        database='SOURCE',
        schema='RAW'
    )
    return conn

def get_data_snowflake(conn):
    """Obtener los datos de la tabla 'subtedata'."""
    cur = conn.cursor()
    try:
        # Ejecutar una consulta para obtener los datos de la tabla 'subtedata'
        cur.execute("SELECT * FROM subtedata")

        # Obtener todos los registros de la tabla
        rows = cur.fetchall()

        # Retornar los datos obtenidos
        return rows
    except Exception as e:
        print("Error al obtener los datos de la tabla 'subtedata':", e)
        return None
    finally:
        cur.close()

# Conectar a Snowflake
conn = conectar_snowflake()

# Obtener los datos de la tabla 'subtedata'
data = get_data_snowflake(conn)

# Guardar los datos como un archivo CSV
if data:
    with open('subte_data_snowflake.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Cerrar la conexión
conn.close()
