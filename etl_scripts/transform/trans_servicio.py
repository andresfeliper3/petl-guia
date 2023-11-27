from datetime import datetime
import petl as etl

def crear_trasn_servicio(urgencias, hospitalizacion, citas):
    cols_seleccionadas = ['codigo_servicio','id_usuario','id_medico','fecha_solicitud','hora_solicitud','fecha_atencion'
        ,'hora_atencion','tipo_servicio']

    #Anadir tipo_servicio
    urgencias = etl.addfield(urgencias,'tipo_servicio','Urgencias')
    hospitalizacion = etl.addfield(hospitalizacion, 'tipo_servicio', 'Hospitalización')
    citas = etl.addfield(citas, 'tipo_servicio', 'Consulta General')

    # Renonbrar campo codigo_servicio
    urgencias = etl.rename(urgencias,'codigo_urgencia','codigo_servicio')
    hospitalizacion = etl.rename(hospitalizacion,'codigo_hospitalizacion','codigo_servicio')
    citas = etl.rename(citas,'codigo_cita','codigo_servicio')

    # unir tablas y seleccionar campos
    transformed_table = etl.cat(urgencias,hospitalizacion,citas)
    transformed_table = etl.cut(transformed_table,cols_seleccionadas)

    #formato fecha_hora
    transformed_table = etl.addfield(transformed_table, 'fecha_hora_atencion', lambda row: datetime.combine(row['fecha_atencion'], row['hora_atencion']))
    transformed_table = etl.addfield(transformed_table, 'fecha_hora_solicitud', lambda row: datetime.combine(row['fecha_solicitud'], row['hora_solicitud']))

    return transformed_table
