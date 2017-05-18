from scraper import Scraper
from aiohttp import ClientSession
import unittest

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()
        self.event_loop = self.scraper.event_loop


    def test_run(self):
        async def wrapper():
            async with ClientSession(loop=self.event_loop) as session:
                self.assertEquals('<!DOCTYPE html>\n<!--[if lt IE 7]>', (await self.scraper.fetch(session, 'https://coinmarketcap.com/all/views/all/'))[0:33] ,'incorect')
        self.event_loop.run_until_complete(wrapper())


    def test_get_table(self):
        async def wrapper():
            async with ClientSession(loop=self.event_loop) as session:
                fetch = await self.scraper.fetch(session, 'https://coinmarketcap.com/all/views/all/')
                table = await self.scraper.get_table(fetch)
                self.assertNotEqual(0, len(table), 'Error')
        self.event_loop.run_until_complete(wrapper())




if __name__ == "__main__":
    unittest.main()

