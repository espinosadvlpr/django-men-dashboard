import pymysql
from datetime import datetime
from sqlalchemy import create_engine, text
from process_data import convert_encoding

print("Cleaning CSV file ...")
data_frame = convert_encoding('./MEN_SNIES.csv')
print("CSV data successfully cleaned. Loading into the database...")

table_name = "men_data_info"
sql_engine = create_engine(
    'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]', pool_recycle=3600)
db_connection = sql_engine.connect()

try:
    frame = data_frame.to_sql(table_name, db_connection, if_exists='replace', index=True, index_label='id')
except ValueError as value_error:
    print(value_error)
except Exception as exception:
    print(exception)
else:
    print(f'Data successfully charged to table {table_name}.')
finally:
    db_connection.close()
