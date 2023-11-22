import petl as etl


def transformar_dim_persona(cotizante, beneficiario, cotizante_beneficiario):
    cols_seleccionadas = ['tipo_documento', 'numero_identificacion', 'nombre', 'fecha_nacimiento', 'sexo',
                          'estado_civil', 'tipo_discapacidad',
                          'tipo_usuario', 'grupo_familiar']

    # añadir constantes a cotizante y duplicar cedula en grupo_familiar
    cotizante = etl.addfield(cotizante, 'tipo_usuario', 'Cotizante')
    cotizante = etl.addfield(cotizante, 'tipo_documento', 'Cedula')
    cotizante = etl.addfield(cotizante, 'grupo_familiar', lambda row: row['cedula'])
    # renombrar y seleccionar campos
    cotizante = etl.rename(cotizante, {'cedula': 'numero_identificacion'})
    cotizante = etl.cut(cotizante, *cols_seleccionadas)

    # añadir constantes a beneficiario
    beneficiario = etl.addfield(beneficiario, 'tipo_usuario', 'Beneficiario')

    # join entre beneficiario y cotizante_beneficiario
    merged_table = etl.join(beneficiario, cotizante_beneficiario, lkey='id_beneficiario', rkey='beneficiario')

    # renombrar y seleccionar campos
    merged_table = etl.rename(merged_table,
                              {'tipo_identificacion': 'tipo_documento', 'id_beneficiario': 'numero_identificacion',
                               'cotizante': 'grupo_familiar'})
    merged_table = etl.cut(merged_table, *cols_seleccionadas)

    # unir las dos tablas iguales
    transformed_table = etl.cat(cotizante, merged_table)

    return transformed_table
