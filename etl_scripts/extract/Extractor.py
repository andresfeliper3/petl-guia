import petl as etl
import yaml

queries_path = 'data_models/extract_queries.yaml'

# Open the YAML file
with open(queries_path, 'r') as file:
    extract_query = yaml.safe_load(file)

# Load data from the source database
class Extractor:
    def __init__(self, source_conn, table_name):
        self.table_name = table_name
        self.source_conn = source_conn

    def extract(self):
        self.table = etl.fromdb(self.source_conn, extract_query[self.table_name])

    def print(self):
        print(etl.look(self.table))

    def get_table(self):
        return self.table
