import sys
import petl as etl
from etl_scripts.managers.managers import dim_managers_dict, trans_managers_dict, fact_managers_dict

EXTRACT_ACTION = 'extract'
TRANSFORM_ACTION = 'transform'
LOAD_ACTION = 'load'
ALL_TABLES = 'all'
DIMENSION_TABLES = 'dimensions'
TRANS_TABLES = 'trans'
FACT_TABLES = 'facts'


def parse_arguments():
    try:
        action = sys.argv[1]
        table = sys.argv[2]
        return action, table
    except IndexError:
        print("Please provide both action and table arguments. Example: py main.py load table_name")
        return None
    except Exception as e:
        print(f"Error parsing command-line arguments: {e}")
        return None


def execute_phases_for_managers(managers, execute_extract, execute_transform, execute_load):
    for manager_instance in managers.values():
        manager_instance.execute_phases(execute_extract, execute_transform, execute_load)


def main():
    args = parse_arguments()
    if args is None:
        sys.exit(1)

    action, table = args

    if action not in [EXTRACT_ACTION, TRANSFORM_ACTION, LOAD_ACTION]:
        print("Please provide a valid action (extract, transform, load).")
        sys.exit(1)

    execute_extract = action in [EXTRACT_ACTION, TRANSFORM_ACTION, LOAD_ACTION]
    execute_transform = action in [TRANSFORM_ACTION, LOAD_ACTION]
    execute_load = action == LOAD_ACTION

    all_managers = dim_managers_dict | trans_managers_dict | fact_managers_dict

    if table == ALL_TABLES:
        all_managers = dim_managers_dict | trans_managers_dict | fact_managers_dict
        execute_phases_for_managers(all_managers, execute_extract, execute_transform, execute_load)
    elif table == DIMENSION_TABLES:
        execute_phases_for_managers(dim_managers_dict, execute_extract, execute_transform, execute_load)
    elif table == TRANS_TABLES:
        execute_phases_for_managers(trans_managers_dict, execute_extract, execute_transform, execute_load)
    elif table == FACT_TABLES:
        execute_phases_for_managers(fact_managers_dict, execute_extract, execute_transform, execute_load)
    else:
        etl_manager = all_managers.get(table)
        if etl_manager:
            etl_manager.execute_phases(execute_extract, execute_transform, execute_load)
        else:
            print(f"Process '{table}' not found.")
            sys.exit(1)


if __name__ == '__main__':
    main()
