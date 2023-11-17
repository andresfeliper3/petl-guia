from etl_scripts.Manager import Manager
from etl_scripts.extract.extractions import medico_extractor
from etl_scripts.transform.dim_medico import dim_medico_transformer
from etl_scripts.load.loaders import dim_medico_loader

dim_medico_manager = Manager(extractor=medico_extractor, transformer=dim_medico_transformer, loader=dim_medico_loader)
