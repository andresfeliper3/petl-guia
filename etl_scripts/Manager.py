import petl as etl


class Manager:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.table = None
        self.transform_function = None

    def extract(self):
        self.extractor.extract()
        self.table = self.extractor.get_table()

    def transform(self, transform_function=None):
        if transform_function is not None:
            self.set_transform_function(transform_function)
        self.transformer.transform(self.table, self.transform_function)
        self.table = self.transformer.get_transformed_table()

    def set_transform_function(self, transform_function):
        self.transform_function = transform_function

    def load(self):
        self.loader.load(self.table)

    def execute_all(self, transform_function=None):
        if transform_function is not None:
            self.set_transform_function(transform_function)
        self.extract()
        self.transform(self.transform_function)
        self.load()

    def print(self):
        print(etl.look(self.table))