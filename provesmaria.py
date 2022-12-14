import mariadb
import sys

try:
    conn = mariadb.connect(
        user="pythonMaster",
        password="Admin1234",
        host="localhost",
        port=3306,
        database="proves"
    )
except mariadb.Error as e:
    print(f"Error conectando a la base de datos: {e}")
    sys.exit(1)

sentenciaSQL = f"""DROP TABLE jugadores
"""
cur = conn.cursor()
cur.execute(sentenciaSQL)
resultado = cur.fetchall()
conn.close()
for i in resultado:
    print(i)


