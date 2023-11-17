from etl_scripts.load.Loader import Loader
from config.db_config import target_conn
from etl_scripts.extract.extractions import ips_extractor

dim_ips_loader = Loader(target_conn=target_conn, table_name="dim_ips")
dim_servicios_loader = Loader(target_conn=target_conn, table_name="dim_servicios")
dim_medico_loader = Loader(target_conn=target_conn, table_name="dim_medico")