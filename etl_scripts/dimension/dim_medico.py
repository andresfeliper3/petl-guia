import petl as etl
from data_models.dimension.dim_medico import create_table_sql, load_sql

TABLE_TARGET_NAME = "dim_medico"

def etl_dim_medico(source_conn, target_conn):
    # Load data from the source database
    table = etl.fromdb(source_conn, load_sql)

    # Apply transformations
    etl.transform.replace(table, 'subespecialidad', '', 'no tine')
    transformed_table = etl.transform.replace(table,'direccion_consultorio','','no registra')

    # Show the transformed data
    etl.look(transformed_table)
    # Create the target table in the target database if it doesn't exist
    create_target_table_manually(transformed_table, target_conn, table_name=TABLE_TARGET_NAME)
    #create_target_table_automatically(transformed_table, target_conn, table_name=TABLE_TARGET_NAME)

def create_target_table_manually(table, target_conn , table_name):
    with target_conn.cursor() as target_cursor:
        target_cursor.execute(create_table_sql)
        target_conn.commit()

    etl.todb(table, target_conn, table_name)

def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=1000)


