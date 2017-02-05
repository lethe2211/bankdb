#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

class BankInfo(object):

    def __init__(self, bcd):
        self.bcd = bcd
        with open('html/{0}.html'.format(bcd), 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'lxml')
            tbody = soup.find('tbody')
            details = tbody.find_all('tr')
            self.attrs = {}
            for detail in details:
                header = detail.find('td', class_='detail-header')
                body = detail.find('td', class_='detail-body')
                if header is not None and body is not None:
                    self.attrs[header.string] = body.string
                    # print('{0}: {1}'.format(header.string, body.string))

    def show(self, attr=None):
        if attr is None:
            return self.attrs
        else:
            return self.attrs[attr]

        
if __name__ == '__main__':
    bcd = sys.argv[1]
    bank_info = BankInfo(bcd)
    print(bank_info.show())
    print(bank_info.show(attr='本店所在地'))
    
