import petl as etl


class Transformer:
    def __init__(self):
        self.table = None
        self.transformed_table = None

    def transform(self, table, transform_function):
        self.table = table
        self.transformed_table = transform_function(self.table)

    def get_transformed_table(self):
        return self.transformed_table

    def get_table(self):
        return self.table

    def print(self):
        print(etl.look(self.transformed_table))
