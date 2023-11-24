from etl_scripts.load.LoaderFactory import LoaderFactory

loader_factory = LoaderFactory()

dim_ips_loader = loader_factory.get_loader(table_name="dim_ips")
dim_servicios_loader = loader_factory.get_loader(table_name="dim_servicios")
dim_medico_loader = loader_factory.get_loader(table_name="dim_medico")
dim_persona_loader = loader_factory.get_loader(table_name="dim_persona")
dim_fecha_loader = loader_factory.get_loader(table_name="dim_fecha")
trans_servicio_loader = loader_factory.get_loader(table_name='trans_servicio')
hecho_atencion_loader = loader_factory.get_loader(table_name='hecho_atencion')
