from etl_scripts.extract.extractions import ips_extractor, medico_extractor, cotizante_extractor, beneficiario_extractor, cotizante_beneficiario_extractor
from etl_scripts.transform.transformers import dim_ips_transformer, dim_servicio_transformer, dim_medico_transformer, dim_persona_transformer
from etl_scripts.load.loaders import dim_ips_loader, dim_medico_loader, dim_servicios_loader, dim_persona_loader
from etl_scripts.Manager import Manager

dim_ips_manager = Manager(extractors=[ips_extractor], transformer=dim_ips_transformer, loader=dim_ips_loader)
dim_medico_manager = Manager(extractors=[medico_extractor], transformer=dim_medico_transformer, loader=dim_medico_loader)
dim_servicios_manager = Manager(transformer=dim_servicio_transformer, loader=dim_servicios_loader)
dim_persona_manager = Manager(extractors=[cotizante_extractor, beneficiario_extractor, cotizante_beneficiario_extractor],
                              transformer=dim_persona_transformer, loader=dim_persona_loader)