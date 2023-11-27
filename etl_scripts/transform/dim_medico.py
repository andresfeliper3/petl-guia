import petl as etl

def transformar_dim_medico(table):
    transformed_table = etl.transform.replace(table, 'subespecialidad', '', 'No registra')
    transformed_table = etl.transform.replace(transformed_table, 'direccion_consultorio', ' ', 'No registra')
    return transformed_table


