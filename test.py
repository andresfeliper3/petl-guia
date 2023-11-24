from datetime import time, date ,datetime

import petl as etl
import psycopg2
from config.env_config import env
conn = psycopg2.connect(
    host=env['db_host'],
    database=env['db_source_name'],
    user=env['db_user'],
    password=env['db_password'],
    port=env['db_port'])

table = etl.fromdb(conn,'select * from urgencias')
table = etl.addfield(table,'fechahora',lambda row: datetime.combine(row['fecha_atencion'],row['hora_atencion']))
print(table['fechahora'])
