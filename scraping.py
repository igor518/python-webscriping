from bs4 import BeautifulSoup
import requests
import pandas as pd

# Specific web scrapping class
class Scrapping:
    PATH = 'https://en.wikipedia.org/wiki/Big_Tech'

    #init scrapping class
    def __init__(self, filename:str)->None:
        self.filename = filename

    # Scrap method
    def scrap(self)->None:
        request = requests.get(self.PATH)
        sp = BeautifulSoup(request.text, 'html.parser')
        table = sp.find_all('table')[1]
        titles = table.find_all("th")
        titles_text = [title.text.strip() for title in titles]
        df=pd.DataFrame(columns=titles_text)
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            value = [col.text.strip() for col in cols]
            df.loc[len(df)] = value
        df.to_csv(self.filename, index=False)

# Only works for the https://en.wikipedia.org/wiki/Big_Tech
if __name__ == '__main__':
    file_path = input('Enter output file path with a name: ')
    scrapping = Scrapping(file_path)
    scrapping.scrap()
