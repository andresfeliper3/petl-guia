# Define the schema and table creation SQL for the target database

create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_medico (
        key_medico BIGSERIAL
        , cedula varchar(40)
        , nombre varchar(100)
        , especialidad VARCHAR(40)
        , sub_especialidad VARCHAR(40)
        , licencia VARCHAR(50)
        , nivel VARCHAR(10)
        , direccion_consultorio VARCHAR(400)
        , id_ips VARCHAR(130)
    );
    """

load_sql = "SELECT * FROM medico"
