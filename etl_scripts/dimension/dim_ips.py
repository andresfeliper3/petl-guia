import petl as etl
from etl_scripts.extract.extractions import ips_extractor
from etl_scripts.transform.transformers import dim_ips_transformer
from etl_scripts.load.loaders import dim_ips_loader
from etl_scripts.Manager import Manager


def transform_dim_ips(table):
    transformed_table = etl.transform.replace(table, 'nivel', '', '0')
    transformed_table = etl.addfield(transformed_table, 'date_from', '2000-01-01')
    transformed_table = etl.addfield(transformed_table, 'date_to', '2030-12-31')
    return transformed_table


dim_ips_manager = Manager(extractor=ips_extractor, transformer=dim_ips_transformer, loader=dim_ips_loader)
dim_ips_manager.extract()
dim_ips_manager.transform(transform_function=transform_dim_ips)
dim_ips_manager.load()

"""
def create_target_table_automatically(table, target_conn, table_name):
    etl.todb(table, target_conn, table_name, create=True, sample=1000)
"""
