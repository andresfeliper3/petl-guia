import petl as etl
from data_models.dimension.dim_ips import create_table_sql, load_sql

TABLE_TARGET_NAME = "dim_ips"

def etl_dim_ips(source_conn, target_conn):
    # Load data from the source database
    table = etl.fromdb(source_conn, load_sql)
    # Apply transformations
    transformed_table = etl.transform.replace(table, 'nivel', '', 0)
    transformed_table = etl.addfield(transformed_table, 'date_from', '2000-01-01')
    transformed_table = etl.addfield(transformed_table, 'date_to', '2030-12-31')
    # Show the transformed data
    print(etl.look(transformed_table))
    # Create the target table in the target database if it doesn't exist
    create_target_table_manually(transformed_table, target_conn, table_name=TABLE_TARGET_NAME)
    #create_target_table_automatically(transformed_table, target_conn, table_name=TABLE_TARGET_NAME)

def create_target_table_manually(table, target_conn, table_name):
    with target_conn.cursor() as target_cursor:
        target_cursor.execute(create_table_sql)
        target_conn.commit()

    etl.todb(table, target_conn, table_name)

def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=1000)


