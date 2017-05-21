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
        #async with session.get(url, headers=headers, proxy="http://10.24.100.210:3128") as response:
        async with session.get(url, headers=headers) as response:
            return await response.text()

    async def get_table(self, html):
        tree = etree.HTML(html)
        table = tree.xpath('//table[@id="currencies-all"]/tbody/tr')
        return table

    def get_row(self, table, i):
        #table = await self.get_table(html)
        name = table[i].xpath('.//td[2]/a/text()')[0]
        symbol = table[i].xpath('.//td[3]/text()')[0]
        market_caps = table[i].xpath('.//td[4]/text()')[0]
        price = table[i].xpath('.//td[5]/a/text()')[0]

        try:
            circulating_supply = table[i].xpath('.//td[6]/a/text()')[0]
        except:
            circulating_supply = table[i].xpath('.//td[6]/span/text()')[0]
        volume = table[i].xpath('.//td[7]/a/text()')[0]
        h1 = table[i].xpath('.//td[8]/text()')[0]
        h24 = table[i].xpath('.//td[9]/text()')[0]
        d7 = table[i].xpath('.//td[10]/text()')[0]
        rov = [name, symbol, market_caps, price, circulating_supply, volume, h1, h24, d7]
        #print(i, self.filter_rov(rov))
        return self.filter_rov(rov)

    def filter_val(self, val):
        val = re.sub(r'\s', '', val)
        #print(val)
        if val == '?' or val == 'LowVol':
            val = 0.0
        else:
            val = Decimal(re.search(r'[0-9|\,|\.|e-]+', re.sub(r'\,', '', val)).group())
        return val

    def filter_rov(self, rov):
        for i in range(2, 9):
            rov[i] = self.filter_val(rov[i])
        return rov


    async def turple_value(self, table, count):
        Name = Symbol = market_cap = Price = Circulating_supply = Volume = h1=  h24 = d7 = list()
        for i in range(0, count):
            row = self.get_row(table, i)
            Name.append(row[0])
            Symbol.append(row[1])
            market_cap.append(row[2])
            Price.append(row[3])
            Circulating_supply.append(row[4])
            Volume.append(row[5])
            h1.append(row[6])
            h24.append(row[7])
            d7.append(row[8])
        self.dic['Name'] = Name
        self.dic['Symbol'] = Symbol
        self.dic['market_cap'] = market_cap
        self.dic['Price'] = Price
        self.dic['Circulating supply'] = Circulating_supply
        self.dic['Volume'] = Volume
        self.dic['h1'] = h1
        self.dic['h24'] = h24
        self.dic['d7'] = d7
    #return self.dic


    async def run(self, loop):
        async with ClientSession(loop=loop) as session:
            html = await self.fetch(session, 'https://coinmarketcap.com/all/views/all/')
            #return await self.turple_value(html)
            table = await self.get_table(html)
            #return self.get_row(table, 0)
            return await self.turple_value(table, 830)

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