import unittest
import scraping
import os

#Test scrapping Unit test class
class TestScrapping(unittest.TestCase):
    # Setting up unit test
    def tearDown(self):
        if os.path.isfile("scraping_text_file.csv"):
            os.remove("scraping_text_file.csv")

    def test_scraping_file(self):
        self.scraping = scraping.Scrapping("scraping_text_file.csv")
        self.scraping.scrap()
        self.assertEqual(os.path.isfile("scraping_text_file.csv"), True)

    def test_is_file_is_not_empty(self):
        self.scraping = scraping.Scrapping("scraping_text_file.csv")
        self.scraping.scrap()
        self.assertNotEqual(os.path.getsize("scraping_text_file.csv"),0)

if __name__ == '__main__':
    unittest.main()
