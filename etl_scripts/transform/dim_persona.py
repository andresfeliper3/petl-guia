import petl as etl


def transformar_dim_persona(cotizante, beneficiario, cotizante_beneficiario):
    merged_table = etl.join(cotizante, cotizante_beneficiario, lkey='cedula', rkey='cotizante')
    merged_table = etl.join(merged_table, beneficiario, lkey='beneficiario', rkey='id_beneficiario')
    # falta rename
    #transformed_table = etl.cut(merged_table, )
    return merged_table
