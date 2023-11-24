from etl_scripts.extract.ExtractorFactory import ExtractorFactory
from config.db_config import source_conn, psa_conn
from etl_scripts.extract.Extractor import Extractor

extractor_factory = ExtractorFactory()

ips_extractor = extractor_factory.get_extractor_source_conn(table_name="ips")
medico_extractor = extractor_factory.get_extractor_source_conn(table_name="medico")

cotizante_extractor = extractor_factory.get_extractor_source_conn(table_name="cotizante")
beneficiario_extractor = extractor_factory.get_extractor_source_conn(table_name="beneficiario")
cotizante_beneficiario_extractor = extractor_factory.get_extractor_source_conn(table_name="cotizante_beneficiario")
urgencias_extractor = extractor_factory.get_extractor_source_conn(table_name="urgencias")
hospitalizacion_extractor = extractor_factory.get_extractor_source_conn(table_name="hospitalizaciones")
citas_extractor =  extractor_factory.get_extractor_source_conn(table_name="citas_generales")
