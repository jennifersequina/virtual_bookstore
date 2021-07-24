import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config

config = read_config('config/config.yaml')

project_id = config['project_id']
credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
client = bigquery.Client(credentials=credentials, project=project_id)

# client.query('select 1 ').to_dataframe()

#df = pd.read_csv('books.csv').rename(columns={'  num_pages':'num_pages'})
#df.to_gbq('dev.books', credentials=credentials, project_id=project_id)


