from etl_scripts.utils.Manager import Manager
import etl_scripts.extract.extractions as ext
import etl_scripts.transform.transformers as trans
import etl_scripts.load.loaders as load

dim_ips_manager = Manager(extractors=[ext.ips_extractor], transformer=trans.dim_ips_transformer,
                          loader=load.dim_ips_loader)
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
hecho_atencion_manager = Manager(extractors=[ext.dim_persona_extractor, ext.dim_medico_extractor, ext.dim_ips_extractor,
                                             ext.dim_fecha_extractor, ext.dim_servicios_extractor,
                                             ext.trans_servicios_extractor],
                                 transformer=trans.hecho_atencion_transfermer, loader=load.hecho_atencion_loader)

managers = {'dim_ips': dim_ips_manager, 'dim_medico': dim_medico_manager, 'dim_servicios': dim_servicios_manager,
            'dim_persona': dim_persona_manager, 'dim_fecha': dim_fecha_manager,
            'trans_servicios': trans_servicio_manager,
            'hecho_atencion': hecho_atencion_manager}
