import os
from dotenv import load_dotenv

load_dotenv()

env = {
    'db_password': os.getenv("DB_PASSWORD"),
    'db_port': os.getenv("DB_PORT"),
    'db_user': os.getenv("DB_USERNAME"),
    'db_host': os.getenv("DB_HOST"),
    'db_target_name': os.getenv("DB_TARGET_NAME"),
    'db_source_name': os.getenv("DB_SOURCE_NAME"),
    'db_psa': os.getenv("DB_PSA_NAME")
}