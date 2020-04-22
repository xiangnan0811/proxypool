# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'https://www.7yip.cn/free/?action=china&page{page}/'
MAX_PAGE = 5


class QYIPCrawler(BaseCrawler):
    """
    daili66 crawler, https://www.7yip.cn/free/?action=china&page=2
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
            address = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            proxy = Proxy(host=address.strip('"'), port=int(port.strip('"')))
            yield proxy


if __name__ == '__main__':
    crawler = QYIPCrawler()
    for proxy in crawler.crawl():
        print(proxy)