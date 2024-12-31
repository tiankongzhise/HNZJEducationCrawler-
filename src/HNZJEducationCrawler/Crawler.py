import requests
import pandas as pd
from collections.abc import Mapping

class ZjCrawler(object):
    def __init__(self, host=None):
        if host is None:
            self.host = 'https://zsxxtp.hnedu.cn/'
        else:
            self.host = host

    def fetch_data(self, url):
        if self.host in url:
            pass
        else:
            url = self.host + url
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise f"Error fetching data from {url}: {e}"

    def parse_data(self, raw_data):
        raise NotImplementedError("parse_data method must be implemented in subclass")

    def save_to_csv(self, data:list | Mapping,
                    columns:list | None=None,
                    filename:str | None=None)->None:
        try:
            df = pd.DataFrame(data)
            if filename is None:
                filename = self.__class__.__name__ + '.csv'
            if columns is not None:
                df.to_csv(filename, index=False)
            else:
                df.to_csv(filename, index=False, header=columns)
        except Exception as e:
            raise f"Error saving data to CSV: {e}"
