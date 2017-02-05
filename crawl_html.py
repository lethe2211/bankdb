#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
import time
import requests
from collections import Counter, defaultdict

if __name__ == '__main__':
    MAX_BCD = 6199
    for index in range(6169, 6169 + 1):
        base_url = 'http://www.opac1.com/bank/detail.php?bcd='        
        print('{0}{1}'.format(base_url, index))

        html = requests.get('{0}{1}'.format(base_url, index)).text
        with open('{0}.html'.format(index), 'w') as f:
            f.write(html)
        time.sleep(3)
