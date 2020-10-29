'''Basic implementation of directed and undirected graphs.'''
class digraph(object):
    '''Class to represent a directed graph.'''
    def __init__(self, v):
        '''Create empty graph with v vertices.'''
        self._V = v             # number of vertices
        self._E = 0             # number of edges.
        # _adj is a list of adjacent vertices, indexed by vertex.
        self._adj = [list() for v in range(self._V)]

    @classmethod
    def fromfile(cls, fp):
        '''Read a graph from a file. Note that this is not the
        format used in the assignment - but you can use this code
        as the basis for code you will need to read the assignment 
        files.'''
        v = int(fp.readline().strip())
        e = int(fp.readline().strip())
        g = cls(v)              # construct the graph.
        for i in range(e):
            v, w = [int(x) for x in fp.readline().split()]
            g.addEdge(v, w)
        return g
    
    def _checkVertex(self, v):
        '''Check if the given vertex is legal.'''
        if v < 0 or v >= self._V:
            raise ValueError('Vertex out of range.')
        
    def adj(self, v):
        '''Get iterable of vertices adjacent to 'v'.'''
        return self._adj[v].copy()
    
    def V(self):
        '''Return the number of vertices in the graph.'''
        return self._V
    
    def E(self):
        '''Return the number of edges in the graph.'''
        return self._E
    
    def __str__(self):
        result = ""
        result += "{} vertices, {} edges\n".format(self._V, self._E)
        for v in range(self._V):
            result += str(v) + ': '
            for w in self._adj[v]:
                result += str(w) + ' '
            result += '\n'
        return result
            
    def addEdge(self, v, w):
        '''Add edge from v to w (directed).'''
        self._checkVertex(v)
        self._checkVertex(w)
        self._adj[v].append(w)
        self._E += 1

    def copy(self):
        '''Return a copy of the graph or digraph.'''
        result = self.__class__(self._V)
        for v in range(self._V):
            for w in self._adj[v]:
                result.addEdge(v, w)
        return result

    def reverse(self):
        '''Create a new digraph with all of the edges reversed.'''
        result = digraph(self._V)
        for v in range(self._V):
            for w in self._adj[v]:
                result.addEdge(w, v)
        return result

class graph(digraph):
    '''Class to represent an undirected graph.'''
    def addEdge(self, v, w):
        '''Add edge from v to w (undirected).'''
        super().addEdge(v, w)  # use superclass for forward edge.
        self._adj[w].append(v) # reverse edge avoids double counting.

    def reverse(self):
        raise ValueError("Can't reverse an undirected graph.")

if __name__ == "__main__":
    # Testing code.
    ug = graph.fromfile(open('tinyG.txt'))
    assert ug.E() == 13 and ug.V() == 13
    assert sorted(ug.adj(0)) == [1, 2, 5, 6]
    dg = digraph.fromfile(open('tinyDG.txt'))
    assert dg.E() == 22 and dg.V() == 13
    assert sorted(dg.adj(0)) == [1, 5]
    rg = dg.reverse()
    assert rg.E() == 22 and rg.V() == 13
    dg = digraph.fromfile(open('mediumDG.txt'))
    assert dg.E() == 147 and dg.V() == 50
    x = ug.copy()
    y = dg.copy()
    assert(type(x) == graph)
    assert(type(y) == digraph)
    print("All tests passed.")

