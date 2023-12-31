from etl_scripts.utils.extract.ExtractorFactory import ExtractorFactory

extractor_factory = ExtractorFactory()

ips_extractor = extractor_factory.get_extractor_source_conn(table_name="ips")
medico_extractor = extractor_factory.get_extractor_source_conn(table_name="medico")

cotizante_extractor = extractor_factory.get_extractor_source_conn(table_name="cotizante")
beneficiario_extractor = extractor_factory.get_extractor_source_conn(table_name="beneficiario")
cotizante_beneficiario_extractor = extractor_factory.get_extractor_source_conn(table_name="cotizante_beneficiario")
urgencias_extractor = extractor_factory.get_extractor_source_conn(table_name="urgencias")
hospitalizacion_extractor = extractor_factory.get_extractor_source_conn(table_name="hospitalizaciones")
citas_extractor = extractor_factory.get_extractor_source_conn(table_name="citas_generales")


dim_persona_extractor = extractor_factory.get_extractor_target_conn(table_name='dim_persona')
dim_medico_extractor = extractor_factory.get_extractor_target_conn(table_name='dim_medico')
dim_ips_extractor = extractor_factory.get_extractor_target_conn(table_name='dim_ips')
dim_fecha_extractor = extractor_factory.get_extractor_target_conn(table_name='dim_fecha')
dim_servicio_extractor = extractor_factory.get_extractor_target_conn(table_name='dim_servicio')
trans_servicios_extractor = extractor_factory.get_extractor_target_conn(table_name='trans_servicios')