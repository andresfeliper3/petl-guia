import petl as etl
from logs.logger import logger_tables_extract, logger_tables_transform, logger_tables_load, logger_process


class Manager:
    def __init__(self, manager_name, extractors=None, transformer=None, loader=None):
        self.manager_name = manager_name
        self.extractors = extractors or []
        self.transformer = transformer
        self.loader = loader
        self.tables = []
        self.transformed_table = None
        self.transform_function = transformer.get_transform_function()

    def extract(self):
        self.check_if_extractors_available()
        for extractor in self.extractors:
            try:
                extractor.extract()
                extracted_table = extractor.get_table()
                if extracted_table is not None:
                    logger_process.info(f"Process {self.manager_name}: table {extractor.get_table_name()} extracted")
                    self.tables.append(extracted_table)
                    logger_tables_extract.info(
                        f"Process {self.manager_name}: table {extractor.get_table_name()} extracted")
                    logger_tables_extract.info(etl.head(extracted_table))  # Move this line here
            except Exception as e:
                logger_process.error(f'Error in process {self.manager_name} extracting data from '
                                     f'{extractor.get_table_name()} table: {e}',
                                     exc_info=True)

    def check_if_extractors_available(self):
        if not self.extractors:
            logger_process.warn(f"Process {self.manager_name}: no extractions defined")

    def transform(self):
        logger_process.info(f"Process {self.manager_name}: transformation in progress for {self.loader.get_table_name()}")
        self.transformer.transform(self.tables)
        self.transformed_table = self.transformer.get_transformed_table()
        logger_tables_transform.info(f"Process {self.manager_name}: Transformation in progress for {self.loader.get_table_name()}")
        logger_tables_transform.info(self.transformed_table)
        logger_process.info(f" Process {self.manager_name}:Transformation complete")

    def load(self):
        self.loader.load(self.transformed_table)
        logger_tables_load.info(self.transformed_table)
        logger_process.info(f"Process {self.manager_name}: table {self.loader.get_table_name()} loaded!")
        logger_tables_load.info(f"Process {self.manager_name}: table {self.loader.get_table_name()} loaded")

    def execute_phases(self, execute_extract: bool, execute_transform: bool, execute_load: bool):
        if execute_extract:
            self.extract()

        if execute_transform:
            self.transform()

        if execute_load:
            self.load()

