from src.HNZJEducationCrawler.crawler_homepage import HomePageCrawler
import unittest


class TestHomePageCrawler(unittest.TestCase):

    def test_call(self):
        crawler = HomePageCrawler()
        result = crawler.run()
        self.assertIsNone(result)