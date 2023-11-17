import petl as etl


class Transformer:
    def __init__(self, transform_function=None):
        self.transform_function = transform_function
        self.table = None
        self.transformed_table = None

    def set_transform_function(self, transform_function):
        self.transform_function = transform_function

    def get_transform_function(self):
        return self.transform_function

    def transform(self, table=None):
        self.table = table
        if self.table is None:
            self.transformed_table = self.transform_function()
        else:
            self.transformed_table = self.transform_function(self.table)

    def get_transformed_table(self):
        return self.transformed_table

    def get_table(self):
        return self.table

    def print(self):
        print(etl.look(self.transformed_table))
