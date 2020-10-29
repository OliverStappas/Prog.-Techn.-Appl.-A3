from collections import deque

def bfs(G, s):
    '''Basic implementation of breadth-first search for Assignment 3.
    Perform BFS from vertex 's', returning lists containing the distances
    and edges (shortest path tree) to each other vertex. A distance of -1
    says that this vertex is not reachable.'''
    distTo = [-1] * G.V() # distance to vertex.
    edgeTo = [-1] * G.V() # edgeTo defines the SPT.

    vertices = deque([s])
    distTo[s] = 0
    while vertices:
        v = vertices.popleft() # get next vertex.
        d = distTo[v] + 1
        for w in G.adj(v):
            if distTo[w] < 0:   # not visited?
                vertices.append(w)
                distTo[w] = d
                edgeTo[w] = v
    return distTo, edgeTo

def pathTo(edgeTo, s, v):
    '''Returns the shortest path from 's' to 'v' as a list of
        integer vertices.'''
    if edgeTo[v] < 0:
        return None             # If no path, return None
    path = []
    x = v                   # Build the path based on the edgeTo values.
    while x != s:
        path = [x] + path
        x = edgeTo[x]
    return [s] + path

if __name__ == "__main__":
    from graph import graph
    G = graph.fromfile(open('tinyG.txt'))
    distTo, edgeTo = bfs(G, 0)
    assert distTo[1] == 1 and pathTo(edgeTo, 0, 1) == [0, 1]
    assert distTo[2] == 1 and pathTo(edgeTo, 0, 2) == [0, 2]
    assert distTo[3] == 2 and pathTo(edgeTo, 0, 3) == [0, 5, 3]
    for v in range(7, G.V()):
        assert distTo[v] < 0 and edgeTo[v] < 0
    print("All tests passed.")
