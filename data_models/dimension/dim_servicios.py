# Define the schema and table creation SQL for the target database

create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_servicios (
        key_s BIGSERIAL
        , date_from DATE
        , date_to DATE

    );
    """

load_sql = "SELECT * FROM dim_servicios "
