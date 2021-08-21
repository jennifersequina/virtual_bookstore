from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config
from typing import List, Dict, Any
import re
config = read_config('config/config.yaml')


class GBQ:
    def __init__(self):
        self.project_id = config['project_id']
        credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
        self.client = bigquery.Client(credentials=credentials, project=self.project_id)

    def search_books(self, search_books: str) -> List[Dict[str, Any]]:
        """
        Method searching for books based on parameter, returns list of matching titles
        :param search_books: String pattern to search
        :return: List of titles
        """

        clean_search_books = self._clean_string(search_books)

        query = f"""
        SELECT title, SPLIT(author, '/')[SAFE_OFFSET(0)] AS author
        FROM `{self.project_id}.dev.books` 
        WHERE LOWER(title)
        LIKE '%{clean_search_books}%'
        OR LOWER(author)
        LIKE '%{clean_search_books}%'
        """

        print(query)
        rows = self.client.query(query=query).result()
        book_list = list()
        for r in rows:
            book_list.append(dict(zip(r.keys(), r.values())))
        return book_list

    @staticmethod
    def _clean_string(str_pattern: str) -> str:
        """
        Remove special characters
        Make lower case
        :param str_pattern: String to clean
        :return: Cleaned string
        """
        # split by space
        list_of_str = list()
        for s in str_pattern.split(" "):
            clean_s = re.sub(r"[^a-zA-Z0-9]+", '', s).lower()
            list_of_str.append(clean_s)
        clean_str = ' '.join(list_of_str)
        clean_str = clean_str.strip()
        print(f"Original: {str_pattern} cleaned: {clean_str}")
        return clean_str

    def get_book_details(self, book_title: str) -> List[Dict[str, Any]]:

        query_details = f"""
                SELECT *
                FROM `{self.project_id}.dev.books` 
                WHERE title = "{book_title}"
                """

        print(query_details)
        rows = self.client.query(query=query_details).result()
        book_details = list()
        for r in rows:
            book_details.append(dict(zip(r.keys(), r.values())))
        return book_details
