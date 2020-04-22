# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'https://ip.ihuan.me/address/5Lit5Zu9.html?page={page}'


class XiaohuanProxyCrawler(BaseCrawler):
    """
    daili66 crawler, https://ip.ihuan.me/address/5Lit5Zu9.html?page=b97827cc
    """
    pages = ['b97827cc', '4ce63706', '5crfe930', 'f3k1d581', 'ce1d45977']
    urls = [BASE_URL.format(page=page) for page in pages]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = etree.HTML(html)
        trs = html.xpath('//table/tbody/tr')
        for tr in trs:
            address = tr.xpath('./td[1]/a/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            proxy = Proxy(host=address.strip('"'), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = XiaohuanProxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)