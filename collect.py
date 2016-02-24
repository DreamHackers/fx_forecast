import asyncio
import urllib.request

class Collector:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.fetch())

    async def fetch(self):
        return await asyncio.wait(
            [self.download(url) for url in self.urls]
        )

    async def download(self, url):
        requst = urllib.request.Request(url)
        html = urllib.request.urlopen(requst).read()
        print("{0} download finish".format(url))
        return html

if __name__ == "__main__":
    collector = Collector([
        "http://fx.formylife.jp/index.html"
    ])

    collector.run()
