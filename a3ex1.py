"""
Oliver Stappas , 1730124
Tuesday , March 19
R. Vincent , instructor
Assignment 3
"""

# Exercise 1

from graph import *
from bfs import *
import math

# Open input file and initialize a directed graph with page numbers
file_name = "J5/" + input("Please enter a file name") + ".in"
file = open(file_name)
nbr_of_pages = int(file.readline())
book_graph = digraph(nbr_of_pages)  # Make a directed graph from 0 to nbr_of_pages - 1

# Construct the graph by adding edges 
for page_number in range(nbr_of_pages):
    next_pages_split = file.readline().split()[1:]  # Actual next pages
    next_pages_list = [int(x) - 1 for x in next_pages_split]  # -1 because v = page nbr - 1, since v  
    for next_page in next_pages_list:                         # starts at 0 and page nbrs start at 1 
        book_graph.addEdge(page_number, next_page)
file.close()        

# BFS to find the shortest distances 
distTo, _ = bfs(book_graph, 0)

# Find min distance to end page and if all pages are reachable 
min_dist = math.inf  # use infinity since any page number < infinity 
reachable = 'Y'
for page, dist in enumerate(distTo):
    if dist > 0 and not book_graph.adj(page):  # If reachable, not fist page and no adjacent vertices
        min_dist = min(min_dist, dist)  # Use running min to find total min
    if dist == -1:
        reachable = 'N'

# Find shortest path length 
shortest_path_len = min_dist + 1  # + 1 because path length includes first page

print(reachable)
print(shortest_path_len)
