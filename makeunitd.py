#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:07:56 2024

@author: vardevol
"""
import math
import copy
import datastructures as d 

def max_claw(intervals, f):
    nbs = intervals.get_nbs(f)
    sol = []
    j = 0
    while j < len(nbs):
        if sol == []:
            sol.append(nbs[0])
        else:
            if nbs[j].l > sol[-1].r :
                sol.append(nbs[j])
        j +=1
    return sol

def find_last(intervals, f):
    nbs = intervals.get_nbs(f)
    ordered_nbs = sorted(nbs, key= lambda i:i.l, reverse = True) 
    return [ordered_nbs[1], ordered_nbs[0]]

def computeB(intervals,f):
    nbs = intervals.get_nbs(f) 
    nbs.append(f)
    snbs = sorted(nbs, key = lambda i :i.l, reverse=True)
    return snbs[0]

def transform3claw(intervals,A, f):
    #compute A1, A2, A3, A4 
    B= find_last(intervals, f)
    #sol = [A[0], A[1], B[0], B[1]]
    i1 = d.Interval(f.label, f.l, A[1].r)
    i2 = d.Interval(f.label, B[0].l, f.r)
    return [i1,i2]

def transform_odd_claw(intervals,A, f):
    n = len(A)
    dint = []
    t = math.ceil(n/2)
    dint.append( d.Interval(f.label, f.l, A[1].r))
    #for every A, I need to find thecorresponding B
    for i in range(2,t-1):
        Bi = computeB(intervals, A[2*i-2])
        dint.append(d.Interval(f.label, Bi.l, A[2*i-1].r))
    dint.append(A[2*t-4])
    lasts = find_last(intervals, f)
    dint.append(d.Interval(f.label, lasts[0].l, f.r))
    return dint 

def transform_even_claw(intervals,A, f):
    n = len(A)
    dint = []
    t = math.ceil(n/2)
    dint.append( d.Interval(f.label, f.l, A[1].r))
    #for every A, I need to find thecorresponding B
    for i in range(2,t):
        Bi = computeB(intervals, A[2*i-2])
        dint.append(d.Interval(f.label, Bi.l, A[2*i-1].r))
    lasts = find_last(intervals, f)
    dint.append(d.Interval(f.label, lasts[0].l, f.r))
    return dint 
    
        
def make_unit(intervals):
    #input is an object of the class representation
    C = copy.copy(intervals.intervals)
    sol = []
    while C != []:
        interval = C.pop()
        #compute maximum number of intersecting disjoint intervals (traverse neighs ordered by end
        #and keep non intersecting ones)
        A = max_claw(intervals, interval)
        n = len(A)
        if n < 3:
            sol.append(interval)
        elif n == 3 :
            sol = sol + transform3claw(intervals, A, interval)
        elif n > 3 and n%2 == 0:
            sol = sol + transform_even_claw(intervals,A, interval)
        elif n > 3 and n%2 == 1:
            sol = sol + transform_odd_claw(intervals, A, interval)
    #returns a list of intervals
    return sol 


#make a parser that transforms the representation of the file to a Representation object 
#parse file into list of int, traverse list, when label is encountered 1st, create int, 
#start or end point is the index on the list.