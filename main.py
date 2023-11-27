# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import petl as etl
from etl_scripts.dimension.managers import managers


def run_etl_all():
    for manager in managers:
        manager.execute_etl()


def run_etl_one_table(manager: str):

    managers[manager].execute_etl()



def run_phase_one_table(manager: str, execute_extract=False, execute_transform=False, execute_load=False):
    if execute_extract:
        managers[manager].extract()

    if execute_transform:
        managers[manager].transform()

    if execute_load:
        managers[manager].load()


def run_phase_all(execute_extract=False, execute_transform=False, execute_load=False):
    for manager in managers:
        if execute_extract:
            manager.extract()

        if execute_transform:
            manager.transform()

        if execute_load:
            manager.load()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ETL_ACTION = 'etl'
    EXTRACT_ACTION = 'extract'
    TRANSFORM_ACTION = 'transform'
    ALL_TABLES = 'all'

    try:
        action = sys.argv[1]
        table = sys.argv[2]

    except:
        print("Invalid arguments")

    if action == EXTRACT_ACTION:
        if table == ALL_TABLES:
            run_phase_all(execute_extract=True)
        else:
            run_phase_one_table(manager=table, execute_extract=True)
    elif action == TRANSFORM_ACTION:
        if table == ALL_TABLES:
            run_phase_all(execute_extract=True, execute_transform=True)
        else:
            run_phase_one_table(manager=table, execute_extract=True, execute_transform=True)
    elif action == ETL_ACTION:
        if table == ALL_TABLES:
            run_etl_all()
        else:
            run_etl_one_table(table)

