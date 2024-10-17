#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:29:43 2024

@author: vardevol
"""

import makeunitd as m 
import parser as p 
import sys 
if len(sys.argv) < 2:
    print("Usage python3 script fileWithIntervalGraph")
    sys.exit()


def main(file):
    """ 
    Input: path to file containing interval graph represented by order of endpoints in a single line as 1 2 2 3 3 1.

    Prints out a list of the intervals, represented by label (name in input, i.e., 1) and interval [x, y] where x and y are points on the real line that mark the endpoints in a $d$-interval representation where no interval intersects three pairwise disjoint intervals.
    """
    list_int = p.parse_to_list(file)
    rep = p.create_representation(list_int)
    unit_rep = m.make_unit(rep)
    unit_rep.sort(key = lambda x :x.l)
    #turn to unit and write on a file
    print(unit_rep)
    p.write_representation(unit_rep, "sol.txt")

graph = sys.argv[1]
if __name__=="__main__":
    main(graph)