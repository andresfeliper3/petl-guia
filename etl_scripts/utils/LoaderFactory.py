from etl_scripts.utils.Loader import Loader
from config.db_config import target_conn


class LoaderFactory:
    def get_loader(self, table_name):
        return Loader(target_conn=target_conn, table_name=table_name)
