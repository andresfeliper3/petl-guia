from etl_scripts.utils.load.Loader import Loader
from config.db_config import target_conn


class LoaderFactory:
    def get_loader(self, table_name):
        return Loader(target_conn_str="postgresql://postgres:310301@localhost:5433/etl_process",
                        table_name=table_name)
