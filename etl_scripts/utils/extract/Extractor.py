import petl as etl
import yaml

queries_path = 'data_models/extract_queries.yaml'

# Open the YAML file
with open(queries_path, 'r') as file:
    extract_query = yaml.safe_load(file)


# Load data from the source database
class Extractor:
    def __init__(self, table_name, source_conn, psa_conn=None, source: bool = False):
        self.table = None
        self.table_name = table_name
        self.source_conn = source_conn
        self.psa_conn = psa_conn
        self.source = source

    def extract(self):
        try:
            self.table = etl.fromdb(self.source_conn, extract_query[self.table_name])
            if self.source:
                pass
                # etl.todb(self.table, self.psa_conn, self.table_name, create=True)

        except Exception as e:
            print(f"Error during extraction for table {self.table_name}: {e}")

    def print(self):
        print(etl.look(self.table))

    def get_table(self):
        return self.table

    def get_table_name(self):
        return self.table_name
