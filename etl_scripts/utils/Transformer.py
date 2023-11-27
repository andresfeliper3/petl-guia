import petl as etl


class Transformer:
    def __init__(self, transform_function=None):
        self.transform_function = transform_function
        self.tables = None
        self.transformed_table = None

    def set_transform_function(self, transform_function):
        self.transform_function = transform_function

    def get_transform_function(self):
        return self.transform_function

    def transform(self, tables=[]):
        self.tables = tables
        if not self.tables:
            self.transformed_table = self.transform_function()
        else:
            self.transformed_table = self.transform_function(*self.tables)

    def get_transformed_table(self):
        return self.transformed_table

    def get_tables(self):
        return self.tables

    def print(self):
        if self.transformed_table is None:
            for table in self.tables:
                print(etl.look(table))
        else:
            print(etl.look(self.transformed_table))
