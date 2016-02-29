import asyncio
import urllib.request
from bs4 import BeautifulSoup

class Collector:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.fetch())

    async def fetch(self):
        return await asyncio.wait(
            [self.scraping(url) for url in self.urls]
        )

    async def scraping(self, url):
        requst = urllib.request.Request(url)
        html = urllib.request.urlopen(requst).read()
        print('{0} download finish'.format(url))
        bs = BeautifulSoup(html, "lxml")

        days_forecast_table = bs.find('strong', string='各社別本日のドル円予想レンジ').parent.parent.parent.parent.parent
        table_file = open('./table_row.txt', 'w')

        table_body = days_forecast_table.find('tbody')
        table_rows = table_body.find_all('tr')
        for row in table_rows:
            table_file.write(row.prettify())
            table_file.write('\nROW------------------------------------------------------------------------------------------------------------------------------------------------------\n')

        print('scraping finish')
        return html

if __name__ == "__main__":
    collector = Collector([
        "http://fx.formylife.jp/index.html"
    ])

    collector.run()
