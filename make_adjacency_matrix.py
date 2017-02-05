#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
import pickle
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

if __name__ == '__main__':
    adj = [[0] * (6199 + 1) for i in range(6199 + 1)]
    for bcd in range(1, 6199 + 1):
        with open('html/{0}.html'.format(bcd), 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'lxml')
            tbody = soup.find('tbody')
            detail_bodies = tbody.find_all('td', class_='detail-body')
            # print(detail_bodies[1].string)
            # print(detail_bodies[4].string)
            # print(detail_bodies[6].string)
            successor_elem = detail_bodies[6]
            successor_atag = successor_elem.find_all('a')
            successors = [e.get('href') for e in successor_atag]
            ans = []
            for s in successors:
                if s.startswith('detail.php?bcd='):
                    succ = int(s[15:])
                    adj[bcd][succ] = 1
    print(adj[:10])
    with open('adj.pickle', 'wb') as f:
        pickle.dump(adj, f)
    
                    
