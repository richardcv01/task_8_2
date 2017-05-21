from scraper import Scraper
from aiohttp import ClientSession
from decimal import Decimal
import unittest

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()
        self.event_loop = self.scraper.event_loop
        self.session = ClientSession(loop=self.event_loop)


    def test_run(self):
        async def wrapper():
            self.assertEquals('<!DOCTYPE html>\n<!--[if lt IE 7]>', (await self.scraper.fetch(self.session, 'https://coinmarketcap.com/all/views/all/'))[0:33] ,'incorect')
        self.event_loop.run_until_complete(wrapper())


    def test_get_table(self):
        async def wrapper():
            fetch = await self.scraper.fetch(self.session, 'https://coinmarketcap.com/all/views/all/')
            table = await self.scraper.get_table(fetch)
            self.assertNotEqual(0, len(table), 'Error')
        self.event_loop.run_until_complete(wrapper())

    def test_filter_val(self):
        val = '?'
        self.assertEquals(self.scraper.filter_val(val), 0.0, 'Errorr')
        val = '$2.8e-08'
        self.assertEquals(self.scraper.filter_val(val), Decimal('2.8e-8'), 'Errorr')
        val = 'Low Vol'
        self.assertEquals(self.scraper.filter_val(val), 0.0, 'Errorr')
        val = '0.25%'
        self.assertEquals(self.scraper.filter_val(val), 0.25, 'Errorr')
        val = '-93.53%'
        self.assertEquals(self.scraper.filter_val(val), Decimal('-93.53'), 'Errorr')

    def test_filter_rov(self):
        rov =  ['Bitcoin', 'BTC', '\n                    $34,085,236,427 \n                ', '$2085.66', '\n                        16,342,662', '$968,381,000', '0.23%', '3.71%', '14.73%']
        filterrov =  ['Bitcoin', 'BTC', Decimal('34085236427'), Decimal('2085.66'), Decimal('16342662'),
                      Decimal('968381000'), Decimal('0.23'), Decimal('3.71'), Decimal('14.73')]
        self.assertEqual(filterrov, self.scraper.filter_rov(rov), 'error')


if __name__ == "__main__":
    unittest.main()

