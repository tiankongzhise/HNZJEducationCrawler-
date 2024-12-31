from .Crawler import ZjCrawler
from bs4 import BeautifulSoup


class HomePageCrawler(ZjCrawler):
    def __init__(self, host=None):
        super().__init__(host)

    def parse_data(self,raw_data):
        soup = BeautifulSoup(raw_data, 'html.parser')
        classification_info = []
        classification_div = soup.find('div', class_='classification fr')
        if classification_div:
            ul = classification_div.find('ul')
            if ul:
                for li in ul.find_all('li', recursive=False):
                    h3 = li.find('h3')
                    p = li.find('p')
                    if h3 and p:
                        category = h3.get_text(strip=True)
                        links = [a['href'] for a in p.find_all('a')]
                        text = [a.get_text(strip=True) for a in p.find_all('a')]
                        # 将 text 和 links 配对，并与 category 形成新的列表结构
                        paired_info = [(category, t, l) for t, l in zip(text, links)]
                        classification_info.extend(paired_info)
        return classification_info

    def run(self,url:str|None = None):
        if url:
            raw_data = self.fetch_data(url)
        else:
            raw_data = self.fetch_data(self.host)
        classification_info = self.parse_data(raw_data)
        colums = ['查询', '学校类型', 'URL']
        result = self.save_to_csv(classification_info,colums)
        return result
