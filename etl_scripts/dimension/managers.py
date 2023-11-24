from etl_scripts.Manager import Manager
import etl_scripts.extract.extractions as ext
import etl_scripts.transform.transformers as trans
import etl_scripts.load.loaders as load

dim_ips_manager = Manager(extractors=[ext.ips_extractor], transformer=trans.dim_ips_transformer, loader=load.dim_ips_loader)
dim_medico_manager = Manager(extractors=[ext.medico_extractor], transformer=trans.dim_medico_transformer,
                             loader=load.dim_medico_loader)
dim_servicios_manager = Manager(transformer=trans.dim_servicio_transformer, loader=load.dim_servicios_loader)
dim_persona_manager = Manager(
    extractors=[ext.cotizante_extractor, ext.beneficiario_extractor, ext.cotizante_beneficiario_extractor],
    transformer=trans.dim_persona_transformer, loader=load.dim_persona_loader)
dim_fecha_manager = Manager(transformer=trans.dim_fecha_transformer, loader=load.dim_fecha_loader)
trans_servicio_manager = Manager(
    extractors=[ext.urgencias_extractor, ext.hospitalizacion_extractor, ext.citas_extractor],
    transformer=trans.trans_servicio_transformer, loader=load.trans_servicio_loader)
