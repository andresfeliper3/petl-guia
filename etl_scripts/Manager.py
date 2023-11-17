import petl as etl


class Manager:
    def __init__(self, extractor=None, transformer=None, loader=None):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.table = None
        self.transform_function = transformer.get_transform_function()

    def extract(self):
        self.extractor.extract()
        self.table = self.extractor.get_table()

    def transform(self):
        self.transformer.transform(self.table)
        self.table = self.transformer.get_transformed_table()

    def load(self):
        self.loader.load(self.table)

    def execute_all(self):
        self.extract()
        self.transform()
        self.load()

    def print(self):
        print(etl.look(self.table))