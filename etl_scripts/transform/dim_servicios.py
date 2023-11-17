import petl as etl
import numpy as np
from etl_scripts.transform.Transformer import Transformer


def crear_dim_servicios():
    # Load data from the source database
    servicios = np.array([('nombre', 'descripcion'), ('Consulta General', 'Servicio de citas medicas'),
                          ('Urgencias', 'Servicio de urgencias'), ('Hospitalizacion', 'Servicio de hospitalizacion')])
    table = etl.wrap(servicios)
    return table


dim_servicios_transformer = Transformer(transform_function=crear_dim_servicios)
