import psycopg2
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