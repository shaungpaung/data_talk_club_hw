import argparse
import os
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url
    
    data_file_name = 'output.csv' 
    
    os.system(f"wget {url} -O {data_file_name}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df = pd.read_csv(data_file_name)
    
    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    
    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    print(f"Data successfully loaded into the {table_name} table.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data into PostgreSQL')
    
    parser.add_argument('--user', help='User name for PostgreSQL', required=True)
    parser.add_argument('--password', help='Password for PostgreSQL', required=True)
    parser.add_argument('--host', help='Host for PostgreSQL', required=True)
    parser.add_argument('--port', help='Port for PostgreSQL', required=True)
    parser.add_argument('--db', help='Database name for PostgreSQL', required=True)
    parser.add_argument('--table_name', help='Name of the table to write to', required=True)
    parser.add_argument('--url', help='URL of the data', required=True)

    args = parser.parse_args()
    main(args)
