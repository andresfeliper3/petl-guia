import pandas as pd
from sqlalchemy import create_engine


class Loader:
    def __init__(self, target_conn_str, table_name):
        self.table = None
        self.target_conn_str = target_conn_str
        self.table_name = table_name
        self.engine = create_engine(self.target_conn_str)

    def _create_table(self):
        if self.table is not None:
            # Explicitly set column names using the header of the DataFrame
            self.table.columns = self.table.iloc[0]
            # New column 'key_ips' with serial values
            self.table.insert(0, 'key_ips', range(1, len(self.table) + 1))
            # Drop the original header row
            self.table = self.table.iloc[1:]

            # Use the modified DataFrame to create the table
            self.table.to_sql(self.table_name, self.engine, index=False, if_exists='replace')

    def load(self, table):
        try:
            self.table = pd.DataFrame(table)  # Convert to DataFrame
            self._create_table()
        except Exception as e:
            print(f"Error during table creation: {e}")

    def insert_into_database(self):
        try:
            # Append new rows to the existing table, or create the table if it doesn't exist
            self.table.to_sql(self.table_name, self.engine, index=False, if_exists='append')
        except Exception as e:
            print(f"Error during data loading: {e}")

    def get_table(self):
        return self.table

    def get_table_name(self):
        return self.table_name
