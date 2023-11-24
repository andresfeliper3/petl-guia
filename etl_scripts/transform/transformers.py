from etl_scripts.transform.Transformer import Transformer
from etl_scripts.transform.dim_ips import transformar_dim_ips
from etl_scripts.transform.dim_medico import transformar_dim_medico
from etl_scripts.transform.dim_servicio import crear_dim_servicio
from etl_scripts.transform.dim_persona import transformar_dim_persona
from etl_scripts.transform.dim_fecha import crear_dim_fecha
from etl_scripts.transform.trans_servicio import crear_trasn_servicio

dim_ips_transformer = Transformer(transform_function=transformar_dim_ips)
dim_medico_transformer = Transformer(transform_function=transformar_dim_medico)
dim_servicio_transformer = Transformer(transform_function=crear_dim_servicio)

dim_persona_transformer = Transformer(transform_function=transformar_dim_persona)

dim_fecha_transformer = Transformer(transform_function=crear_dim_fecha)
trans_servicio_transformer = Transformer(transform_function=crear_trasn_servicio)


def trans_servicio_loader():
    return None