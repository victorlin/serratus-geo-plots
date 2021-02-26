import pandas as pd
from sqlalchemy import create_engine

endpoint = 'serratus-aurora-20210225.cluster-ro-ccz9y6yshbls.us-east-1.rds.amazonaws.com'
database = 'summary'
username = 'public_reader'
password = 'serratus'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{endpoint}/{database}')

def download(query):
    with engine.connect() as con:
        df = pd.read_sql(query, con)
    return df
