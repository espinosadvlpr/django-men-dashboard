from sqlalchemy import create_engine, text
import pandas as pd
import pymysql
from datetime import datetime

data_frame = pd.read_csv("./MEN_SNIES_test_original.csv", engine="python", encoding="utf-8")
print("CSV data successfully charged...")

table_name = "men_data_info_csv"
sql_engine = create_engine(
    'mysql+pymysql://root:mysql123@127.0.0.1/men_dashboard_db', pool_recycle=3600)
db_connection = sql_engine.connect()

try:
    frame = data_frame.to_sql(table_name, db_connection, if_exists='append')
except ValueError as value_error:
    print(value_error)
except Exception as exception:
    print(exception)
else:
    db_connection.execute(text("insert into men_data_info (ies, sector_ies, caracter_ies, departamento_domicilio_ies, municipio_domicilio_ies, programa_academico, nivel_academico, nivel_formacion, metodologia, sexo, anio, semestre, graduados, matriculados) select ies, sector_ies, caracter_ies, departamento_domicilio_ies, municipio_domicilio_ies, programa_academico, nivel_academico, nivel_formacion, metodologia, sexo, anio, semestre, graduados, matriculados from men_data_info_csv;"))
    db_connection.commit()
    print("Data successfully charged to table men_data_info")
finally:
    db_connection.close()
