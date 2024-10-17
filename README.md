# From-interval-to-unit-d--interval

<h1> Unit 2-interval graph checker  </h1>

This python script transforms a given interval graph into a unit $d$-interval graph for the smallest $d$ possible.



**Usage**  

To run the code run the following command:

```bash
python3 main.py graph_file.txt
```

The file "graph_file.txt" must contain a list of interval graphs in the format described in http://www.jaist.ac.jp/~uehara/graphs/ .  
That is, each interval graph is represented in one line in a simple text format, e.g., 1 1 2 2 3 3 (independent set of three vertices), 1 2 1 3 2 3 (path of length 3), 1 2 3 3 2 1 (complete graph of size 3). 


**Output**  

Prints out a list of intervals, represented by label (name in input, i.e., 1) and interval [x, y] where x and y are points on the real line that mark the endpoints in a $d$-interval representation where no interval intersects three pairwise disjoint intervals. Furthermore, it creates a file "sol.txt" where the unit $d$-interval representation is given as in the input format (i.e., list of ordered enpoints). 
