import petl as etl
from logs.logger import logger_tables, logger_process


class Manager:
    def __init__(self, extractors=None, transformer=None, loader=None):
        self.extractors = extractors or []
        self.transformer = transformer
        self.loader = loader
        self.tables = []
        self.transformed_table = None
        self.transform_function = transformer.get_transform_function()

    def extract(self):
        if not self.extractors:
            logger_process.warn("No extractions defined")

        for extractor in self.extractors:
            try:
                extractor.extract()
                logger_process.info(f"Table {extractor.get_table_name()} extracted")
                extracted_table = extractor.get_table()
                logger_tables.info(extracted_table)
                self.tables.append(extracted_table)
            except Exception as e:
                logger_process.error(f'Error in extracting data from {extractor.get_table_name()} table: {e}', exc_info=True)

    def transform(self):
        logger_process.info("Transformation in progress")
        self.transformer.transform(self.tables)
        self.transformed_table = self.transformer.get_transformed_table()
        logger_process.info("Transformation complete")

    def load(self):
        self.loader.load(self.transformed_table)
        logger_process.info(f"Table {loader.get_table_name()} loaded!")

    def execute_etl(self):
        self.extract()
        self.transform()
        self.load()

    def print(self):
        if self.transformed_table is None:
            for table in self.tables:
                print(etl.look(table))
        else:
            print(etl.look(self.transformed_table))
