# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re

BASE_URL = 'http://cn-proxy.com/'


class CnProxyCrawler(BaseCrawler):
    """
    ip3366 crawler, http://cn-proxy.com/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
        # \s * 匹配空格，起到换行作用
        re_ip_address = ip_address.findall(html)[2:]
        for address, port in re_ip_address:
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = CnProxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)