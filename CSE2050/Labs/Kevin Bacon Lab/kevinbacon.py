import time
import random

class Queue:
    def __init__(self, L):
        self._L = L
        def enqueue(self, item):
            self._L.append(item)

        def dequeue(self, item):
            return self._L.pop(0)

        def __len__(self):
            return len(self._L)

        def isempty(self):
            return len(self) == 0

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

    def bfs(self, V):
        t = {}
        t[V] = None
        q = [V]
        while q != []:
            current = q.pop(0)
            for i in self.neighbors(current):
                if i not in t:
                    t[i] = current
                    q.append(i)
        return t


    def help(self, u, v):
        a = list(u.keys())[0]
        b = [v]
        c = v
        while c != a:
            try:
                c = u[c]
            except KeyError:
                return None
            b = [c] + b
        return b

    def findPath(self, u, v):
        if u == v:
            return None
        x = self.bfs(u)
        return self.help(x, v)


def getMapAtoM():
  fp = open("lg_actor_data.txt", "r")
  mapAtoM = {}
  for s in fp:
    if not s.strip():
      continue

    #print(s)
    l1 = s.split("\t")
    if s[0].isalpha():
      actor = l1[0].split("(")[0].strip()
    movie = l1[-1].split(")")[0].strip() + ')'
    #print ("ACTOR:",actor)
    #print("MOVIE:", movie)

    if actor not in mapAtoM:
      mapAtoM[actor] = set([movie])
    elif movie not in mapAtoM[actor]:
      mapAtoM[actor].add(movie)

  fp.close()
  return mapAtoM

## Use the SimpleUGraph from the previous lab

def createActorGraph(mapAtoM):
    #G = SimpleUGraph(mapAtoM)
    #return G
    G = SimpleUGraph(set(), set())
    m = mapAtoM
    for actors in m.keys():
        G.addVertex(actors)
    for actor1 in m.keys():
        for actor2 in m.keys():
            if actor1 == actor2:
                pass
            else:
                for movie in m[actor1]:
                    if movie in m[actor2]:
                        G.addEdge(actor1, actor2)
    return G

def KBNcompute(G, actor):
    if actor == "Bacon, Kevin":
        return 0
    else:
        if G.findPath("Bacon, Kevin", actor) is None:
            return float("inf")
        else:
            return (len(G.findPath("Bacon, Kevin", actor)) - 1)
