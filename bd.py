import psycopg2

DB_NAME="milestone"
DB_USER="postgres"
DB_PASS="vagsZa5r"
DB_HOST="localhost"
DB_PORT="5432"

try:
    con=psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    cur=con.cursor()

    print('conexion exitosa')

    cur.execute('SELECT version();')
    db_version=cur.fetchone()
    print(f'la version de la bd es {db_version}')

except psycopg2.Error as e:
    print(f'Error al conectar o consultar la base de datos: {e}')

finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()
    print('conexion cerrada')

