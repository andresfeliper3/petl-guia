import petl as etl

def crear_hecho_atencion(persona, medico, ips, fecha,servicios,trans_servicios):
    persona = etl.cut(persona, 'key_persona', 'numero_identificacion')
    merge1 = etl.join(persona, trans_servicios, lkey='numero_identificacion', rkey='id_usuario')
    medico = etl.cut(medico, 'key_medico', 'cedula', 'id_ips')
    merge2 = etl.join(merge1, medico, lkey='id_medico', rkey='cedula')
    dim_ips = etl.cut(ips, 'key_ips', 'id_ips')
    merge3 = etl.join(ips, merge2)
    servicios = etl.cut(servicios, 'key_servicio', 'nombre')
    merge4 = etl.join(merge3, servicios, rkey='nombre', lkey='tipo_servicio')
    fecha1 = etl.cut(fecha, 'key_date', 'date')
    fecha1 = etl.rename(fecha1, 'key_date', 'key_date_atencion')
    fecha2 = etl.rename(fecha1, 'key_date_atencion', 'key_date_solicitud')
    merge5 = etl.join(merge4, fecha1, lkey='fecha_atencion', rkey='date')
    merge6 = etl.join(merge5, fecha2, lkey='fecha_solicitud', rkey='date')

    merge6 = etl.addfield(merge6, 'tiempo_espera_dias',
                          lambda row: (row['fecha_hora_atencion'] - row['fecha_hora_solicitud']).days)
    merge6 = etl.addfield(merge6, 'tiempo_espera_minutos',
                          lambda row: (row['fecha_hora_atencion'] - row['fecha_hora_solicitud']).seconds // 60)
    merge6 = etl.addfield(merge6, 'tiempo_espera_horas', lambda row: row['tiempo_espera_minutos'] // 60)
    merge6 = etl.cut(merge6, 'key_ips', 'key_persona', 'key_tran_servicio', 'key_medico', 'key_servicio',
                     'key_date_atencion', 'key_date_solicitud', 'tiempo_espera_dias', 'tiempo_espera_minutos',
                     'tiempo_espera_horas')
    return merge6