import sys
import os

class Graph:

    def __init__(self,filename=None,delimiter=None):
        self._edges = 0
        self._adj = dict()

        if filename is not None :
            pass


    def add_edge(self,v,w):
        if not self.has_vertex(v) : self._adj[v] = set()
        if not self.has_vertex(w) : self._adj[w] = set()
        if not self.has_edge(v,w):
            self._edges += 1
            self._adj[v].add(w)
            self._adj[w].add(v)

            return True

        return False

    def adjacent_to(self,v):
        return iter(self._adj[v])

    def vertices(self):
        return iter(self._adj)

    def has_vertex(self,v):
        return (v in self._adj)

    def has_edge(self,v,w):
        return (w in self._adj[v])

    def count_edges(self):
        return self._edges

    def __len__(self):
        return self.count_edges()

    def degree(self,v):
        return len(self._adj[v])

    def __str__(self):
        s = ''

        for v in self.vertices():
            s += (str(v) + ' : ')
            for w in self.adjacent_to(v):
                s += (str(w) + ' ')
            s += '\n'

        return s

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_file(file_name,delimiter=","):

        if file_name is not None:
            graph = Graph()
            with open(file_name,'r') as file:
                for line in file:
                    elements = line.split(delimiter)
                    for i in range(1,len(elements)):
                        graph.add_edge(elements[0],elements[i])

            return graph
        else :
            raise TypeError(f'File name has to be given')



