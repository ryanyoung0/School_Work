import time
import random

class Graph:
    def addVertex(self, vert):
        #Add a vertex with key k to the vertex set.
        raise NotImplemented

    def addEdge(self, fromVert, toVert):
        #Add a directed edge from u to v.
        raise NotImplemented

    def neighbors(self):
        #Return an iterable collection of the keys of all
        #vertices adjacent to the vertex with key v.
        raise NotImplemented

    def removeEdge(self, u, v):
        #Remove the edge from vertex u to v from graph.
        raise NotImplemented

    def removeVertex(self, v):
        #Remove the vertex v from the graph as well as any edges
        #incident to v.
        raise NotImplemented

    ## Part 2
    def dfs(self, v):   # shold be good now
        d = {}
        q = [(None, v)]
        while q:
            x, y = q.pop()
            if y not in d:
                d[y] = x
                for i in self.neighbors(y):
                    q.append((y, i))
        return d

    def bfs(self, V):
        t = {}
        tv = Queue([(None, v)])
        while tv:
            x, y = tv.dequeue()
            if y not in t:
                t[y] = x
                for i in self.neighbors(y):
                    tv.enqueue((y, i))
        return t


    def findPath(self, u, v):
        ps = self.dfs(u)
        p = []
        if u == v:
            return None
        elif v in ps:
            p.append(v)
            current = v
            while ps[current] is not None:
                p.append(ps[current])
                current = ps[current]
            p.reverse()
            return p
        else:
            return None


class SimpleGraph(Graph):
    def __init__(self, V, E):
        self._V = set()
        self._E = set()
        for v in V: self.addVertex(v)
        for u, v in E: self.addEdge(u, v)


    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def addVertex(self, v):
        self._V.add(v)

    def addEdge(self, u, v):
        self._E.add((u, v))

    def neighbors(self, v):
        return (w for u, w in self._E if u == v)

    def removeEdge(self, u, v):
        self._E.remove((u, v))

    def removeVertex(self, v):
        for neighbor in list(self.neighbors(v)):
            self.removeEdge(v, neighbor)
        self._V.remove(v)

## Part 1
class SimpleUGraph(SimpleGraph):
    def addEdge(self, u, v):
        self._E.add((u, v))
        self._E.add((v, u))

    def removeEdge(self, u, v):
        self._E.remove((u, v))
        self._E.remove((v, u))


## Part 3
class AdjacencyListGraph(Graph):
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V:
            self.addVertex(v)
        for u, v in E:
            self.addEdge(v, u)
          # need to get a function to return the neighbors of
         # the key includes the vertex the value will contain just the neighbors of that
         #vertex
                                                #a singular node and return them
    def addEdge(self, v, u):
        self._nbrs[u].add(v)

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def neighbors(self, v):
        return iter(self._nbrs[v])

    def hasedge(self, u, v):
        return v in self._nbrs[u]

    def removeEdge(self, u, v=None):
        self._nbrs[u].remove(v)

    def addVertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield(u,v)

    def removeVertex(self, V):
        self._V.remove(V)

class AdjacencyListUGraph(AdjacencyListGraph):
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V:
            self.addVertex(v)
        for u, v in E:
            self.addEdge(v, u)
          # need to get a function to return the neighbors of
         # the key includes the vertex the value will contain just the neighbors of that
         #vertex
                                                #a singular node and return them
    def addEdge(self, v, u):
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def hasedge(self, u, v):
        return v in self._nbrs[u]

    def removeEdge(self, u, v):
        self._nbrs[u].remove(v)
        self._nbrs[v].remove(u)


    def addVertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield(u,v)

    def removeVertex(self, V):
        self._V.remove(V)
        for x in list(self.nbrs(V)):
            self.removeEdge(V, x)



## Part 4
class AdjacencyMatrixGraph(AdjacencyListGraph):
    def __init__(self, V, E):
        self._edges = set()
        self._V = list()
        self._E = list()
        for i in V:
            self.addVertex(i)
        for u, v in E:
            self.addEdge(u, v)
        # need to recurse over something so that we can add in the edge at the coordinates of the edge put the one in there
        # then need to fill in the zeros wheere

    def edges(self):
        Lst = []
        x = 0
        y = 0
        for i in self._E:
            for j in i:
                if j == 1:
                    Lst.append( (self._V[x], self._V[y]) )
                y += 1
            x += 1
            y = 0
        return iter(Lst)

    def vertices(self):
        return self._V

    def addVertex(self, v):
        self._V.append(v)
        NR = [0]
        for r in self._E:
            r.append(0)
            NR.append(0)
        self._E.append(NR)

    def removeVertex(self, v):
        index = self._V.index(v)
        for r in self._E:
            r.pop(index)
        self._E.pop(index)
        self._V.remove(v)

    def neighbors(self, v):
        ns = []
        index = self._V.index(v)
        sum = 0
        for n in self._E[index]:
            if n == 1:
                ns.append(self._V[sum])
            sum += 1
        return ns

    def matrix(self):
        return self._E

    def addEdge(self, u, v):
        x = self._V.index(u)
        y = self._V.index(v)
        self._E[x][y] = 1

    def removeEdge(self, u, v):
        x = self._V.index(u)
        y = self._V.index(v)
        self._E[x][y] = 0

class AdjacencyMatrixUGraph(AdjacencyMatrixGraph):
    def addEdge(self, u, v):
        x = self._V.index(u)
        y = self._V.index(v)
        self._E[x][y] = 1    #How we get the ones to appear in the matrix
        self._E[y][x] = 1    # need to somehow make sure formatiing is correct
                            # in our list of lists potential

    def removeEdge(self, u, v):
        x = self._V.index(u)
        y = self._V.index(v)
        self._E[x][y] = 0
        self._E[y][x] = 0
