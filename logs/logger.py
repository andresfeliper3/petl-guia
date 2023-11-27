import logging
import os
from datetime import datetime

logs_folder = 'logs'
os.makedirs(logs_folder, exist_ok=True)


def configure_logger(logger_name, log_folder):
    os.makedirs(log_folder, exist_ok=True)

    today_date = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(log_folder, f'{today_date}.log')

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file, mode='a')  # 'a' for append
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Example usage
logger_process = configure_logger('process', os.path.join(logs_folder, 'process'))
logger_tables = configure_logger('tables', os.path.join(logs_folder, 'tables'))
