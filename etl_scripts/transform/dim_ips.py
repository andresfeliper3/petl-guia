import petl as etl
from etl_scripts.transform.Transformer import Transformer
from etl_scripts.extract.extractions import ips_extractor


def transform_dim_ips(table):
    transformed_table = etl.transform.replace(table, 'nivel', '', '0')
    transformed_table = etl.addfield(transformed_table, 'date_from', '2000-01-01')
    transformed_table = etl.addfield(transformed_table, 'date_to', '2030-12-31')
    return transformed_table


dim_ips_transformer = Transformer(transform_function=transform_dim_ips)
