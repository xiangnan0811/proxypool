# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.goubanjia.com/'


class GoubanjiaCrawler(BaseCrawler):
    """
    daili66 crawler, http://www.goubanjia.com/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = etree.HTML(html)
        tds = html.xpath('//td[@class="ip"]')
        for td in tds:
            address = ''.join(td.xpath('./*[not(@style="display: none;")]/text()')[:-1])
            port = td.xpath('./*[not(@style="display: none;")]/text()')[-1]
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = GoubanjiaCrawler()
    for proxy in crawler.crawl():
        print(proxy)