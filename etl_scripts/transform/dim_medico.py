import petl as etl
from etl_scripts.transform.Transformer import Transformer
from etl_scripts.extract.extractions import medico_extractor


def transform_dim_medico(table):
    transformed_table = etl.transform.replace(table, 'subespecialidad', '', 'No registra')
    transformed_table = etl.transform.replace(transformed_table, 'direccion_consultorio', ' ', 'No registra')
    return transformed_table


dim_medico_transformer = Transformer(transform_function=transform_dim_medico)
