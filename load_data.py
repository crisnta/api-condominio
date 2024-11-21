import sqlite3
import json
import psycopg2
import sys

def load_data_sqlite(json_file):
    """ Cargar datos en SQLite """
    conn = sqlite3.connect('condominios.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe, incluyendo el campo de ubicación
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS condominio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL  -- Agregado campo para ubicación
    )
    ''')
    conn.commit()

    # Leer el archivo JSON
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Insertar los datos en la tabla
    for item in data:
        cursor.execute('INSERT INTO condominio (name, location) VALUES (?, ?)', (item['name'], item['location']))

    conn.commit()
    conn.close()
    print("Datos cargados en SQLite.")

def load_data_postgresql(json_file):
    """ Cargar datos en PostgreSQL """
    conn = psycopg2.connect(
        dbname='tu_db',
        user='tu_usuario',
        password='tu_contraseña',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    # Crear la tabla si no existe, incluyendo el campo de ubicación
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS condominio (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        location TEXT NOT NULL  -- Agregado campo para ubicación
    )
    ''')
    conn.commit()

    # Leer el archivo JSON
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Insertar los datos en la tabla
    for item in data:
        cursor.execute('INSERT INTO condominio (name, location) VALUES (%s, %s)', (item['name'], item['location']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Datos cargados en PostgreSQL.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python load_data.py <sqlite/postgresql> <ruta_al_archivo_json>")
        sys.exit(1)

    db_type = sys.argv[1].lower()
    json_file = sys.argv[2]

    if db_type == 'sqlite':
        load_data_sqlite(json_file)
    elif db_type == 'postgresql':
        load_data_postgresql(json_file)
    else:
        print("Tipo de base de datos no soportado. Usa 'sqlite' o 'postgresql'.")