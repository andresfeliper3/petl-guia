from etl_scripts.extract.Extractor import Extractor
from config.db_config import source_conn

ips_extractor = Extractor(source_conn=source_conn, table_name="ips")
medico_extractor = Extractor(source_conn=source_conn, table_name="medico")

