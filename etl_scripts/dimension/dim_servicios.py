import petl as etl
import numpy as np
from data_models.dimension.dim_servicios import create_table_sql

TABLE_TARGET_NAME = "dim_servicios"

def etl_dim_servicios(source_conn, target_conn):
    # Load data from the source database
    servicios = np.array([('nombre','descripcion'),('Consulta General', 'Servicio de citas medicas'),('Urgencias', 'Servicio de urgencias'),('Hospitalizacion', 'Servicio de hospitalizacion')])
    table = etl.wrap(servicios)

    table.look()

    # Create the target table in the target database if it doesn't exist
    create_target_table_manually(table, target_conn, table_name=TABLE_TARGET_NAME)
    #create_target_table_automatically(transformed_table, target_conn, table_name=TABLE_TARGET_NAME)

def create_target_table_manually(table, target_conn, table_name):
    with target_conn.cursor() as target_cursor:
        target_cursor.execute(create_table_sql)
        target_conn.commit()

    etl.todb(table, target_conn, table_name)

def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=1000)


