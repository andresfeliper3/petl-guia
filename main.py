# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import psycopg2
import petl as etl
from config.env_config import env


source_conn = psycopg2.connect(
    host=env['db_host'],
    database=env['db_source_name'],
    user=env['db_user'],
    password=env['db_password'],
    port=env['db_port']
)

target_conn = psycopg2.connect(
    host=env['db_host'],
    database=env['db_target_name'],
    user=env['db_user'],
    password=env['db_password'],
    port=env['db_port']
)


def etl_dim_ips():
    # Load data from the source database
    table = etl.fromdb(source_conn, 'SELECT * FROM ips')
    # Apply transformations
    transformed_table = etl.cutout(table, 'nivel')
    transformed_table = etl.addfield(transformed_table, 'date_from', '2000-01-01')
    transformed_table = etl.addfield(transformed_table, 'date_to', '2030-12-31')
    # Show the transformed data
    etl.look(transformed_table)
    # Create the target table in the target database if it doesn't exist
    create_target_table_manually(transformed_table, target_conn, 'dim_ips')
    #create_target_table_automatically(transformed_table, target_conn, 'dim_ips')



def create_target_table_manually(table, target_conn, table_name):
    create_target_ips_table()
    etl.todb(table, target_conn, table_name)

def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=100)

def create_target_ips_table():
    # Define the schema and table creation SQL for the target database
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_ips (
        key_ips BIGSERIAL
        , date_from DATE
        , date_to DATE
        , id_ips VARCHAR(40)
        , tipo_ips VARCHAR(40)
        , nombre VARCHAR(300)
        , direccion VARCHAR(400)
        , municipio VARCHAR(400)
        , departamento VARCHAR(400)
    );
    """

    # Execute the SQL to create the table
    with target_conn.cursor() as target_cursor:
        target_cursor.execute(create_table_sql)
        target_conn.commit()


def close_connections(*connections):
    for conn in connections:
        if conn:
            conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        etl_dim_ips()
    finally:
        close_connections(source_conn, target_conn)
