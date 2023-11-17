from etl_scripts.extract.extractions import ips_extractor
from etl_scripts.transform.dim_ips import dim_ips_transformer
from etl_scripts.load.loaders import dim_ips_loader
from etl_scripts.Manager import Manager

dim_ips_manager = Manager(extractor=ips_extractor, transformer=dim_ips_transformer, loader=dim_ips_loader)


"""
def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=1000)
"""
