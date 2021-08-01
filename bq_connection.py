import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config

config = read_config('config/config.yaml')

project_id = config['project_id']
credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
client = bigquery.Client(credentials=credentials, project=project_id)


 # importing csv file to bigquery
# df = pd.read_csv('data/books with category.csv').rename(columns={'Name': 'title',
#                                                                  'Author': 'author',
#                                                                  'User Rating': 'user_rating',
#                                                                  'Reviews': 'reviews',
#                                                                  'Price': 'price',
#                                                                  'Year': 'year',
#                                                                  'Genre': 'genre'})
# df.to_gbq('dev.books_category', credentials=credentials, project_id=project_id)



