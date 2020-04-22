# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
import re
from lxml import etree
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.xiladaili.com/gaoni/{page}/'
MAX_PAGE = 5


class XiladailiCrawler(BaseCrawler):
    """
    daili66 crawler, http://www.xiladaili.com/gaoni/1/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        ip_address = re.compile('<tr>\s*<td>(.*?)</td>')
        # \s * 匹配空格，起到换行作用
        re_ip_address = ip_address.findall(html)
        for ip in re_ip_address:
            address, port = ip.split(':')
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = XiladailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)