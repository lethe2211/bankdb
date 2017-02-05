#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
import pickle
from collections import Counter, defaultdict

import pydot

from bank_info import BankInfo

if __name__ == '__main__':
    initial = int(sys.argv[1])
    with open('adj.pickle', 'rb') as f:
        adj = pickle.load(f)
        stack = [initial]

        di_graph = pydot.Dot(graph_type='digraph')
        while stack != []:
            bcd = stack.pop()
            print(bcd)
            bank_info = BankInfo(bcd)
            bcd_node = pydot.Node(bcd, label=bank_info.show(attr='銀行名'))
            di_graph.add_node(bcd_node)

            for nxt, connected in enumerate(adj[bcd]):
                if connected == 1:
                    nxt_bank_info = BankInfo(nxt)

                    nxt_node = pydot.Node(nxt, label=nxt_bank_info.show(attr='銀行名'))
                    di_graph.add_node(nxt_node)
                    
                    edge = pydot.Edge(bcd, nxt)
                    di_graph.add_edge(edge)
                    
                    stack.append(nxt)
        di_graph.write_jpeg('result_from_{}.jpeg'.format(initial), prog='dot')
