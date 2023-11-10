# Define the schema and table creation SQL for the target database

create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_persona (
        key_persona BIGSERIAL
        , tipo_documento varchar(40)
        , numero_identificacion varchar(40)
        , nombre varchar(100)
        , tipo_usuario VARCHAR(40)
        , estado_civil VARCHAR(40)
        , sexo VARCHAR(50)
        , fecha_nacimiento VARCHAR(10)
        , grupo_familiar VARCHAR(400)
        , tipo_discapacidad VARCHAR(130)
    );
    """

load_sql = dict(beneficiario='select * from beneficiario', cotizante='select * from cotizante',
                cotizante_beneficiario='select * form cotizante_beneficiario')
