# Define the schema and table creation SQL for the target database

create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_servicios (
        key_servicio BIGSERIAL
       , nombre VARCHAR(50)
       , descripcion VARCHAR (50)
    );
    """

#load_sql = "SELECT * FROM dim_servicios "
