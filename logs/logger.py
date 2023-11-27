import logging
import os
from datetime import datetime

logs_folder = 'logs'
os.makedirs(logs_folder, exist_ok=True)


def configure_logger(logger_name, log_folder, subfolder=None, to_file=True, to_console=True):
    os.makedirs(log_folder, exist_ok=True)

    if subfolder:
        log_folder = os.path.join(log_folder, subfolder)
        os.makedirs(log_folder, exist_ok=True)

    today_date = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(log_folder, f'{today_date}.log')

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if to_file:
        file_handler = logging.FileHandler(log_file, mode='a')  # 'a' for append
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# Example usage
logger_process = configure_logger('process', os.path.join(logs_folder, 'process'))
logger_tables_extract = configure_logger('extract', os.path.join(logs_folder, 'tables'), subfolder='extract', to_console=True)
logger_tables_transform = configure_logger('transform', os.path.join(logs_folder, 'tables'), subfolder='transform',
                                           to_console=False)
logger_tables_load = configure_logger('load', os.path.join(logs_folder, 'tables'), subfolder='load', to_console=False)