import petl as etl
import yaml

queries_path = 'data_models/load_queries.yaml'

# Open the YAML file
with open(queries_path, 'r') as file:
    load_query = yaml.safe_load(file)


class Loader:
    def __init__(self, target_conn, table_name):
        self.table = None
        self.target_conn = target_conn
        self.table_name = table_name

    def load(self, table):
        self.table = table
        with self.target_conn.cursor() as target_cursor:
            target_cursor.execute(load_query[self.table_name])
            self.target_conn.commit()

        etl.todb(self.table, self.target_conn, self.table_name)

    def get_table(self):
        return self.table

    def get_table_name(self):
        return self.table_name