from etl_scripts.utils.Manager import Manager
import etl_scripts.extract.extractions as ext
import etl_scripts.transform.transformers as trans
import etl_scripts.load.loaders as load


def create_manager(manager_name, extractors=None, transformer=None, loader=None):
    return Manager(manager_name=manager_name, extractors=extractors, transformer=transformer, loader=loader)


dim_managers_dict = {
    'dim_ips': create_manager('dim_ips', extractors=[ext.ips_extractor], transformer=trans.dim_ips_transformer,
                              loader=load.dim_ips_loader),
    'dim_medico': create_manager('dim_medico', extractors=[ext.medico_extractor],
                                 transformer=trans.dim_medico_transformer, loader=load.dim_medico_loader),
    'dim_servicio': create_manager('dim_servicio', transformer=trans.dim_servicio_transformer,
                                   loader=load.dim_servicio_loader),
    'dim_persona': create_manager('dim_persona', extractors=[ext.cotizante_extractor, ext.beneficiario_extractor,
                                                             ext.cotizante_beneficiario_extractor],
                                  transformer=trans.dim_persona_transformer, loader=load.dim_persona_loader),
    'dim_fecha': create_manager('dim_fecha', transformer=trans.dim_fecha_transformer, loader=load.dim_fecha_loader),
}

trans_managers_dict = {
    'trans_servicio': create_manager(
        'trans_servicio',
        extractors=[ext.urgencias_extractor, ext.hospitalizacion_extractor, ext.citas_extractor],
        transformer=trans.trans_servicio_transformer,
        loader=load.trans_servicio_loader
    )
}

fact_managers_dict = {
    'hecho_atencion': create_manager(
        'hecho_atencion',
        extractors=[
            ext.dim_persona_extractor, ext.dim_medico_extractor, ext.dim_ips_extractor,
            ext.dim_fecha_extractor, ext.dim_servicio_extractor, ext.trans_servicios_extractor
        ],
        transformer=trans.hecho_atencion_transformer,
        loader=load.hecho_atencion_loader
    )
}
