# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.data5u.com/'


class Data5uCrawler(BaseCrawler):
    """
    daili66 crawler, http://www.data5u.com/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = etree.HTML(html)
        trs = html.xpath('//ul[@class="l2"]')
        for tr in trs:
            address = tr.xpath('./span[1]/li/text()')[0]
            port = tr.xpath('./span[2]/li/text()')[0]
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = Data5uCrawler()
    for proxy in crawler.crawl():
        print(proxy)