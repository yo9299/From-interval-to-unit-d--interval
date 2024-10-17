#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:18:34 2024

@author: vardevol
"""

class Interval:
    def __init__(self, label, start, end): #, neighbors):
        self.label = label
        self.l = start
        self.r = end 
    
    def update_start(self, new_start):
        self.l = new_start
        
    def update_end(self, new_end):
        self.r = new_end
        
    def get_length(self):
        return self.r - self.l 
        
    def __str__(self):
        return f"Label: {self.label}, Interval: [{self.l}, {self.r}]"
    
    def __repr__(self):
        return f"Label: {self.label}, Interval: [{self.l}, {self.r}]"
        
class Representation:
    #initialize with list of intervals
    def __init__(self, intervals):
        self.intervals = intervals
        
    def __str__(self):
        return "\n".join(str(i) for i in self.intervals)
        """ 
        sol = "" 
        for i in self.intervals:
            sol = sol + "[" + str(i.l) + "," + str(i.r) + "]" + "\n"
        return sol
        """
        
    def get_nbs(self, interval):
        #get them in order of 
        nbs = []
        for i in self.intervals:
            if i != interval:
                if not (i.r < interval.l or i.l > interval.r):
                    nbs.append(i)
                """     
                if i.l >= interval.l and i.l <= interval.r:
                    nbs.append(i)
                elif i.r >= interval.l and i.r <= interval.r:
                    nbs.append(i)
                elif i.l <= interval.l and i.r >= interval.r:
                    nbs.append(i)
                elif i.l >= interval.l and i.r <= interval.r:
                    nbs.append(i)
                """
        return sorted(nbs, key= lambda i:i.r) 
    


A = Interval(1, 1, 16)
B = Interval(2, 1, 3)
C= Interval(3, 4, 5)
D = Interval(4, 6, 7)
D0 = Interval(9, 6.5, 7.5)
E = Interval(5, 8,11)
F = Interval(6, 12, 13)
G = Interval(7, 14, 15)
H= Interval(8, 16,16)
rep = Representation([A,B,C,D, E, F, G, H, D0])