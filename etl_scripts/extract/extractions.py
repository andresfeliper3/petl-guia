from etl_scripts.extract.Extractor import Extractor
from config.db_config import source_conn,psa_conn

ips_extractor = Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name="ips")
medico_extractor = Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name="medico")

cotizante_extractor = Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name="cotizante")
beneficiario_extractor = Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name="beneficiario")
cotizante_beneficiario_extractor = Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name="cotizante_beneficiario")
