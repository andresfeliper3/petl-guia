from etl_scripts.extract.Extractor import Extractor
from config.db_config import target_conn, source_conn, psa_conn


class ExtractorFactory:
    def get_extractor_source_conn(self, table_name):
        return Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name=table_name)

    def get_extractor_target_conn(self, table_name):
        return Extractor(source_conn=target_conn, psa_conn=psa_conn, table_name=table_name)