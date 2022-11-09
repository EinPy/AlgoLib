# Intution for maximal flow #

In a directed graph, find the max amount of 
paths from a to b withouth shared edges

A simple method is to travel from a to b and remove all edges that are used, but this does not always give the best answer. One can
actually reverse all the edges that are used

To see actual paths you can take all the edges that have been 
reversed an odd number of times and reverse them again, to see
all the simple paths from a to b. 