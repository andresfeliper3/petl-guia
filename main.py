# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import petl as etl
from config.db_config import source_conn, target_conn
from etl_scripts.dimension import dim_ips, dim_servicios, dim_medico


def close_connections(*connections):
    for conn in connections:
        if conn:
            conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        dim_ips.etl_dim_ips(source_conn, target_conn)
        dim_medico.etl_dim_medico(source_conn, target_conn)
        dim_servicios.etl_dim_servicios(source_conn, target_conn)

    finally:
        close_connections(source_conn, target_conn)
