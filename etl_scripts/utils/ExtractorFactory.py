from etl_scripts.utils.Extractor import Extractor
from config.db_config import target_conn, source_conn, psa_conn


class ExtractorFactory:

    def __init__(self):
        self.tables = []

    def get_extractor_source_conn(self, table_name):
        if table_name in self.tables:
            return Extractor(source_conn=psa_conn, table_name=table_name)
        else:
            self.tables.append(table_name)
            return Extractor(source_conn=source_conn, psa_conn=psa_conn, table_name=table_name, source=True)

    def get_extractor_target_conn(self, table_name):
        return Extractor(source_conn=target_conn, table_name=table_name)
