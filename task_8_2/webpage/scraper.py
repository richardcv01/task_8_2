import asyncio
from aiohttp import ClientSession
from lxml import etree
import re
from decimal import Decimal


class Scraper():

    def __init__(self):
        self.dic = dict()
        self.event_loop = asyncio.SelectorEventLoop()

    async def fetch(self, session, url):
        headers = {'Host': 'coinmarketcap.com',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'uk,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        async with session.get(url, headers=headers, proxy="http://10.24.100.210:3128") as response:
            return await response.text()

    async def get_table(self, html):
        tree = etree.HTML(html)
        table = tree.xpath('//table[@id="currencies-all"]/tbody/tr')
        print(table)
        return table

    async def element(self, html):
        table = await self.get_table(html)

        name = table[0].xpath('.//td[2]/a/text()')[0]
        symbol = table[0].xpath('.//td[3]/text()')[0]
        market_caps = table[0].xpath('.//td[4]/text()')[0]
        price =  market_cap = table[0].xpath('.//td[5]/a/text()')[0]
        circulating_supply = table[0].xpath('.//td[6]/a/text()')[0]
        volume = table[0].xpath('.//td[7]/text()')[0]
        h1 = table[0].xpath('.//td[8]/text()')[0]
        h24 = table[0].xpath('.//td[9]/text()')[0]
        d7 = table[0].xpath('.//td[10]/text()')[0]



   #tr/td[3]/text()

    async def turple_value(self, html):
        tree = etree.HTML(html)
        chb1 = r'[0-9|\,|\.]+'
        sub1 = r'\s', ''
        table = tree.xpath('//table[@id="currencies-all"]')
        print(table)
        self.dic['Name'] = table[0].xpath('//td[@class="no-wrap currency-name"]/a/text()')
        self.dic['Symbol'] = table[0].xpath('//td[@class="text-left"]/text()')

        self.dic['market_cap'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                                 table[0].xpath('//td[@class="no-wrap market-cap text-right"]/text()') ]
        self.dic['Price'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(r'[0-9|\,|\.]+', re.sub(r'\,', '', s)).group()) for s in
                       table[0].xpath('//a[@class="price"]/text()')]
        table_obj = table[0].xpath('//tr[@id="id-bond"]')
        self.dic['Circulating supply'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                                                table_obj[0].xpath('//td[5]/a/text()')]
        self.dic['Volume'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                         table_obj[0].xpath('//td[6]/a/text() | //td[6]/span/text()')]
        self.dic['h1'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                  table_obj[0].xpath('//td[8]/text() | //td[8]/span/text()')]
        self.dic['h24'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                    table_obj[0].xpath('//td[9]/text() | //td[9]/span/text()')]
        self.dic['d7'] = [0 if re.sub(r'\s', '', s)=='?' else Decimal(re.search(chb1, re.sub(r'\,', '', s)).group()) for s in
                  table_obj[0].xpath('//td[10]/text() | //td[10]/span/text()')]

    #return name, symbol, market_cap, price, circulating_supply, volume, h1, h24, d7


    async def run(self, loop):
        async with ClientSession(loop=loop) as session:
            html = await self.fetch(session, 'https://coinmarketcap.com/all/views/all/')
            #return await self.turple_value(html)
            return await self.element(html)

    def return_data(self):
        #event_loop = asyncio.SelectorEventLoop()
        asyncio.set_event_loop(self.event_loop)
        try:
            self.event_loop.run_until_complete(self.run(self.event_loop))
        finally:
            self.event_loop.close()
        return self.dic

S = Scraper()
print(S.return_data())