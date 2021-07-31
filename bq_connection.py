import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config

config = read_config('config/config.yaml')

project_id = config['project_id']
credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
client = bigquery.Client(credentials=credentials, project=project_id)


# query creation
query = """
    SELECT *
    FROM `virtual-bookstore-320810.dev.books` 
    WHERE title
    LIKE '%Anne%'
"""
query_job = client.query(query)
rows = query_job.result()

for row in rows:
    print(row.title)


#  importing csv file to bigquery
# df = pd.read_csv('books.csv').rename(columns={'  num_pages':'num_pages'})
# df.to_gbq('dev.books', credentials=credentials, project_id=project_id)


