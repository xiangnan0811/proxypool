# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""
from retrying import retry
import requests
from loguru import logger

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
}


class BaseCrawler(object):
    urls = []

    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None)
    def fetch(self, url, **kwargs):
        try:
            response = requests.get(url, headers=headers, **kwargs)
            if response.status_code == 200:
                return response.text
        except requests.ConnectionError:
            return

    @logger.catch
    def crawl(self):
        """
        crawl main method
        """
        for url in self.urls:
            logger.info(f'fetching {url}')
            html = self.fetch(url)
            for proxy in self.parse(html):
                logger.info(f'fetched proxy {proxy.string()} from {url}')
                yield proxy