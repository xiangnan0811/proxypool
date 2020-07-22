# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re
from lxml import etree

BASE_URL = 'https://www.kuaidaili.com/free/inha/{page}/'


class KuaidailiCrawler(BaseCrawler):
    """
    kuaidaili crawler, https://www.kuaidaili.com/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, 20)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        # doc = pq(html)
        html = etree.HTML(html)
        trs = html.xpath('//table//tr')
        for tr in trs[1:]:
            ip = tr.xpath('./td[@data-title="IP"]/text()')[0]
            port = tr.xpath('./td[@data-title="PORT"]/text()')[0]
            if ip and port:
                yield Proxy(host=ip, port=port)


if __name__ == '__main__':
    crawler = KuaidailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)