# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import petl as etl
from etl_scripts.dimension.dim_ips import dim_ips_manager
from etl_scripts.dimension.dim_servicios import dim_servicios_manager
from etl_scripts.dimension.dim_medico import dim_medico_manager

execute_extract = True
execute_transform = True
execute_load = True


def run():
    if execute_extract:
        dim_ips_manager.extract()
        dim_medico_manager.extract()

    if execute_transform:
        dim_ips_manager.transform()
        dim_servicios_manager.transform()
        dim_medico_manager.transform()

    if execute_load:
        dim_ips_manager.load()
        dim_servicios_manager.load()
        dim_medico_manager.load()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
