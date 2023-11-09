# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import petl as etl
from config.db_config import source_conn, target_conn
from etl_scripts.dimension.dim_ips import etl_dim_ips

def close_connections(*connections):
    for conn in connections:
        if conn:
            conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        etl_dim_ips(source_conn, target_conn)
    finally:
        close_connections(source_conn, target_conn)
