import sys
import os
from collections import defaultdict

class UGraph:

    def __init__(self):
        self._edges = 0
        self._adj = defaultdict(set)

    def __len__(self):
        return self._edges

    def __contains__(self, node):
        return (node in self._adj)

    def __str__(self):
        return f"UGraph <{len(self._adj)}, {self._edges}>"

    def __repr__(self):
        return str(self)

    @property
    def edges(self):
        visited = set()
        for v in self._adj:
            visited.add(v)
            for w in self._adj[v]:
                if w not in visited:
                    yield (v, w)

    @property
    def nodes(self):
        for v in self._adj.keys():
            yield v

    def add_node(self, v):
        if v not in self._adj:
            self._adj[v]
            return True
        else:
            return False

    def add_edge(self, v, w):
        if not self.has_edge(v,w):
            self._edges += 1
            self._adj[v].add(w)
            self._adj[w].add(v)
            return True

        return False

    def remove_node(self, node):
        if node in self._adj:
            for v in self._adj[node]:
                self._edges -= 1 # removing edges
                self._adj[v].remove(node)
            del self._adj[node]
            return True
        else:
            return False

    def remove_edge(self, v, u):
        if self.has_edge(v, u):
            self._edges -= 1
            self._adj[v].remove(u)
            self._adj[u].remove(v)
            return True
        else:
            return False

    def has_node(self, v):
        return (v in self._adj)

    def has_edge(self,v,w):
        if v in self._adj:
            return (w in self._adj[v])
        else:
            return False

    def count_edges(self):
        return self._edges

    def count_nodes(self):
        return len(self._adj)

    def adjacent(self, v, lazy=True):
        if v in self._adj:
            method = iter if lazy else set
            return method(self._adj[v])
        else:
            return set()

    def degree(self, v):
        if v in self._adj:
            return len(self._adj[v])
        else:
            return -1 # or raise an error

    def weight(self, v, u):
        if self.has_edge(v, u):
            return 1
        else:
            return float('inf')

    @staticmethod
    def from_file(file_name,delimiter=","):

        if file_name is not None:
            graph = UGraph()
            with open(file_name,'r') as file:
                for line in file:
                    elements = line.split(delimiter)
                    for i in range(1,len(elements)):
                        graph.add_edge(elements[0],elements[i])

            return graph
        else :
            raise TypeError(f'File name has to be given')


class WGraph(UGraph):

    def __init__(self):
        self._edges = 0
        self._adj = defaultdict(dict)

    @property
    def edges(self):
        visited = set()
        for v in self._adj:
            visited.add(v)
            for w in self._adj[v].keys():
                if w not in visited:
                    yield (v, w)

    def add_edge(self, v, u, weight=1):
        if not self.has_edge(v, u):
            self._edges += 1
        self._adj[v][u] = weight
        self._adj[u][v] = weight
        return True

    def remove_node(self, node):
        if node in self._adj:
            for v in self._adj[node]:
                self._edges -= 1 # removing edges
                self._adj[v].pop(node)
            del self._adj[node]
            return True
        else:
            return False

    def remove_edge(self, v, u):
        if self.has_edge(v, u):
            self._edges -= 1
            self._adj[v].pop(u)
            self._adj[u].pop(v)
            return True
        else:
            return False


    def weight(self, v, u):
        if self.has_edge(v, u):
            return self._adj[v][u]
        else:
            return float('inf')
