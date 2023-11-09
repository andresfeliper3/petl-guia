# Define the schema and table creation SQL for the target database

create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_ips (
        key_ips BIGSERIAL
        , date_from DATE
        , date_to DATE
        , id_ips VARCHAR(40)
        , tipo_ips VARCHAR(40)
        , nombre VARCHAR(300)
        , direccion VARCHAR(400)
        , municipio VARCHAR(400)
        , departamento VARCHAR(400)
    );
    """

load_sql = """SELECT * FROM ips"""
