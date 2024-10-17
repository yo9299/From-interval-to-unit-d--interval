#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:48:39 2024

@author: vardevol
"""
import datastructures as d 

#given list of ints, create list of intervals -> return an object of representation


def parse_to_list(file):
    """
    Reads a file containing a single line of space-separated integers and 
    converts it into a list of integers, which represents the ordered 
    endpoints of the intervals of a representation.

    Args:
        file (str): The path to the file containing ordered interval endpoints.

    Returns:
        list: A list of integers representing ordered interval endpoints.
    
    Example:
        Input file content: "1 2 2 3 3 1"
        Output: [1, 2, 2, 3, 3, 1]
    """
    with open(file, "r") as rep:
        # Read the entire file as a single string and split by spaces, 
        # then convert to integers in a single step
        return list(map(int, rep.read().split()))
    '''rep = open(file, "r")
    line = rep.read() #lines()
    #line = [l for l in info]
    rep.close()
    data = line[0].split(" ")
    list_int = [int(i) for i in data]
    return list_int''' 
    

def create_representation(input_list):
    """
    Constructs a representation of intervals based on a list of ordered endpoints. 
    Each integer in the list corresponds to an interval's start or end point, 
    processed in sequence to either open or close intervals.

    Args:
        input_list (list): A list of integers representing ordered interval endpoints.
                           Each integer denotes either the start or end of an interval.

    Returns:
        Representation: An object representing the intervals and their structure.
    
    Example:
        Input: [1, 2, 2, 3, 3, 1]
        Output: Representation of intervals on the real line with start and end points being integers on the real line.
    """
    open_intervals = {}
    for i, point in enumerate(input_list):
        if point not in open_intervals:
            open_intervals[point] = d.Interval(point, i, i)
        else:
            open_intervals[point].update_end(i)
    return d.Representation(list(open_intervals.values()))
    """ 
    i = 0 #is the counter of the real line point we are in
    j = 0 
    open_intervals = []
    while j < len(input_list):
        interval = [ o for o in open_intervals if o.label == input_list[j]]
        if interval == []:
            open_intervals.append(d.Interval(input_list[j], i, i))
        else:
            interval[0].update_end(i) 

        i +=1 
        j +=1
    #returns an object of representation
    return d.Representation(open_intervals)
    """

def write_representation(intervals, filename):
    endpoints = []
    for i in intervals:
        endpoints.append((i.label, i.l))
        endpoints.append((i.label, i.r))
    ordered = sorted(endpoints, key= lambda x: x[1])
    sol = [x[0] for x in ordered]
    with open(filename, "w") as file:
        file.write(" ".join(map(str, sol)))
