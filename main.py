
import sys
import petl as etl
from etl_scripts.dimension.managers import managers_dict


def run_etl_all():
    for manager in managers_dict.values():
        manager.execute_etl()


def run_etl_one_table(manager: str):
    managers_dict[manager].execute_etl()


def run_phase_one_table(manager: str, execute_extract=False, execute_transform=False, execute_load=False):
    if execute_extract:
        managers_dict[manager].extract()

    if execute_transform:
        managers_dict[manager].transform()

    if execute_load:
        managers_dict[manager].load()


def run_phase_all(execute_extract=False, execute_transform=False, execute_load=False):
    for manager in managers_dict.values():
        if execute_extract:
            manager.extract()

        if execute_transform:
            manager.transform()

        if execute_load:
            manager.load()


if __name__ == '__main__':
    LOAD_ACTION = 'load'
    EXTRACT_ACTION = 'extract'
    TRANSFORM_ACTION = 'transform'
    ALL_TABLES = 'all'

    try:
        action = sys.argv[1]
        table = sys.argv[2]
    except IndexError:
        print("Please provide both action and table arguments.")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing command-line arguments: {e}")
        sys.exit(1)

    if action in [EXTRACT_ACTION, TRANSFORM_ACTION, LOAD_ACTION]:
        execute_extract = action == EXTRACT_ACTION or action == TRANSFORM_ACTION or action == LOAD_ACTION
        execute_transform = action == TRANSFORM_ACTION or action == LOAD_ACTION
        execute_load = action == LOAD_ACTION

        if table == ALL_TABLES:
            run_phase_all(execute_extract, execute_transform, execute_load)
        else:
            run_phase_one_table(manager=table, execute_extract=execute_extract, execute_transform=execute_transform,
                                execute_load=execute_load)
    else:
        print(f"Please provide a valid action (extract, transform, load).")
