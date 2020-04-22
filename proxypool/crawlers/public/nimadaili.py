# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.nimadaili.com/gaoni/{page}'
MAX_PAGE = 5


class NimadailiCrawler(BaseCrawler):
    """
    daili66 crawler, http://www.nimadaili.com/gaoni/2/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = etree.HTML(html)
        trs = html.xpath('//table/tbody/tr')
        for tr in trs:
            ip = tr.xpath('./td[1]/text()')[0]
            address, port = ip.split(':')
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = NimadailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)