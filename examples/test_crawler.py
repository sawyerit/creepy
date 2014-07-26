#!/usr/bin/env python

from creepy import Crawler
from threading import Lock

class TestCrawler(Crawler):
    def __init__(self):
        super(TestCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        self.process_lock.acquire()
        print 'GET', doc.status, doc.url
        self.process_lock.release()

crawler = TestCrawler()
crawler.set_follow_mode(Crawler.F_ANY)
crawler.set_concurrency_level(100)
crawler.add_url_filter('\.(jpg|jpeg|gif|png|js|css|swf)$')
crawler.crawl('http://www.msn.com/')
