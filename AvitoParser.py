import httpx


class AvitoParser:
    url: str = ""

    def __init__(self, url: str):
        self.url = url

    def createCSV(self):
        r = httpx.get(self.url)
        print(r)