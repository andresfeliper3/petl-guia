from etl_scripts.load.loaders import dim_servicios_loader
from etl_scripts.transform.dim_servicios import dim_servicios_transformer
from etl_scripts.Manager import Manager

dim_servicios_manager = Manager(transformer=dim_servicios_transformer, loader=dim_servicios_loader)





