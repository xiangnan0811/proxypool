# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'https://www.xicidaili.com/nn/{page}'
MAX_PAGE = 5


class XicidailiCrawler(BaseCrawler):
    """
    daili66 crawler, https://www.xicidaili.com/nn/2
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('#ip_list tr:gt(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(2)').text()
            port = int(tr.find('td:nth-child(3)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = XicidailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)