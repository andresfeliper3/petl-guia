import petl as etl
import numpy as np


def crear_dim_servicio():
    # Load data from the source database
    servicios = np.array([('nombre', 'descripcion'), ('Consulta General', 'Servicio de citas medicas'),
                          ('Urgencias', 'Servicio de urgencias'), ('Hospitalización', 'Servicio de hospitalizacion')])
    table = etl.wrap(servicios)
    return table


