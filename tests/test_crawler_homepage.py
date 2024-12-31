from src.HNZJEducationCrawler.crawler_homepage import HomePageCrawler
import unittest


class TestHomePageCrawler(unittest.TestCase):
    def setUp(self) -> None:
        self.crawler = HomePageCrawler()