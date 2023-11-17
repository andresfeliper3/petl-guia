import petl as etl


class Manager:
    def __init__(self, extractors=None, transformer=None, loader=None):
        self.extractors = extractors or []
        self.transformer = transformer
        self.loader = loader
        self.tables = []
        self.transformed_table = None
        self.transform_function = transformer.get_transform_function()

    def extract(self):
        for extractor in self.extractors:
            extractor.extract()
            self.tables.append(extractor.get_table())

    def transform(self):
        self.transformer.transform(self.tables)
        self.transformed_table = self.transformer.get_transformed_table()

    def load(self):
        self.loader.load(self.transformed_table)

    def execute_all(self):
        self.extract()
        self.transform()
        self.load()

    def print(self):
        if self.transformed_table is None:
            for table in self.tables:
                print(etl.look(table))
        else:
            print(etl.look(self.transformed_table))
