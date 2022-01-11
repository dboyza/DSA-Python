
"""
 UNDIRECTED, UNWEIGHTED GRAPH 
 ADJACENCY LIST IMPLEMENTATION
"""


# Graph Implementation; Adjacency List
class Graph:
    # Graph constructor
    def __init__(self):
        self.adj_list = {}

    # Adds a vertex to the graph: O(1)
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Adds a vertex from the graph: O(|V| + |E|)
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    # Adds an undirected edge to the graph: O(1)
    def add_edge(self, v1, v2):
        # Adds the edge if the vertices exist in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # Removes an undirected edge from the graph: O(|E|)
    def remove_edge(self, v1, v2):
        # Removes the edge if the vertices exist in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    # Prints the graph
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.remove_edge('C', 'A')

graph.remove_vertex('D')

graph.print_graph()
