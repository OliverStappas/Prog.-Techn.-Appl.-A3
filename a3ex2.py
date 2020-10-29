"""
Oliver Stappas , 1730124
Tuesday , March 19
R. Vincent , instructor
Assignment 3
"""

# Exercise 2

from graph import *
from bfs import *
import math

# Open input file and initialize a directed graph with page numbers
file_name = "J5/" + input("Please enter a file name") + ".in"
file = open(file_name)
nbr_of_pages = int(file.readline())
book_graph = digraph(nbr_of_pages)

# Construct the graph by adding edges
for page_number in range(nbr_of_pages):
    next_pages_split = file.readline().split()[1:]  # Actual next pages
    next_pages_list = [int(x) - 1 for x in next_pages_split]  # -1 because v = page nbr - 1, since v
    for next_page in next_pages_list:                         # starts at 0 and page nbrs start at 1
        book_graph.addEdge(page_number, next_page)
file.close()

# BFS to find the shortest distances
distTo, _ = bfs(book_graph, 0)

# Find min and max distances to end page, if all pages are reachable and end pages
min_dist = math.inf
max_dist = -math.inf
reachable = 'Y'
end_pages_list = []
for page, dist in enumerate(distTo):
    if dist > 0 and not book_graph.adj(page):  # If reachable, not fist page and no adjacent vertices
        min_dist = min(min_dist, dist)  # Use running min to find total min
        max_dist = max(max_dist, dist)  # Use running max to find total max
        end_pages_list.append(page)
    if dist == -1:
        reachable = 'N'

# Find the number of paths of length equal to the shortest path
nbr_paths_eq_to_shortest = 0
for page in end_pages_list:
    if distTo[page] == min_dist:
        nbr_paths_eq_to_shortest += 1

# Find shortest and longest path lengths (path length = dist + 1 because path length includes first page)
shortest_path_len = min_dist + 1
longest_path_len = max_dist + 1

print(reachable)
print(shortest_path_len)
print(nbr_paths_eq_to_shortest)
print(longest_path_len)
