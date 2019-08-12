from vertex import Vertex
from file_reader import FileReader
from queue import Queue


class ADTGraph(object):
    def __init__(self, FILE_PATH=None):
        self.f = FileReader(FILE_PATH)
        self.vertices = {}  # dictionary of verticies
        self.edges = []
        self.vertex_count = 0
        self.edge_count = 0
        self.digraph = None
        self.start = None
        if FILE_PATH is not None:
            all_verticies = self.f.verticies
            self.edges = self.f.edges
            self.digraph = self.f.digraph
            self.add_verticies(all_verticies)
            self.add_egdes(self.edges)

    def __iter__(self):
        '''yields each vertex key'''
        '''traverses the graph in BFS order from a start'''
        for vert in self.vertices:
            yield vert

    def __contains__(self, key):
        return key in self.vertices

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        if self.start is None:
            self.start = vert
        if not vert in self.vertices:
            self.vertices[vert] = Vertex(vert)
            self.vertex_count += 1

    def add_verticies(self, verts):
        for vert in verts:
            self.add_vertex(vert)

    def get_vertex(self, vert_key):
        '''finds the vertex in the graph named vertKey. Or returns None if not found'''
        if vert_key in self.vertices:
            return self.vertices[vert_key]

    def add_edge(self, from_key, to_key, weight=1):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        if from_key not in self.vertices:
            raise KeyError(f'{from_key} vertex not found in graph')
        if to_key not in self.vertices:
            raise KeyError(f'{to_key} vertex not found in graph')
        if self.get_vertex(from_key).is_pointing_to(to_key):
            return
        self.get_vertex(from_key).points_to(to_key, int(weight))
        self.edge_count += 1
        self.edges.append((from_key, to_key))
        if self.digraph is False:
            self.get_vertex(to_key).points_to(from_key, weight)

    def add_egdes(self, edges):
        for edge in edges:
            self.add_edge(*edge)

    def get_vertices(self):
        '''returns the list of all vertices in the graph.'''
        return [vertex for vertex in self]

    def get_neighbor_keys(self, x):
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        return list(x.neighbors.keys())

    def get_neighbors(self, x):
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        # return [neighbor for neighbor in x.neighbors.values()]
        return list(x.neighbors.values())

    def breadth_first_search(self, start):
        '''traverses the graph in BFS order from a start'''
        seen = {start}
        queue = Queue([start])
        print(start)
        while not queue.is_empty():
            vertex_key = queue.dequeue()
            for neighbor in self.get_vertex(vertex_key).neighbors:
                if neighbor not in seen:
                    print(neighbor)
                    seen.add(neighbor)
                    queue.enqueue(neighbor)
        return list(seen)

    def shortest_path(self, start, end: str):
        '''finds the shortest path between two points and returns None if there are none'''
        seen = {start: [start]}
        queue = Queue([start])
        while not queue.is_empty():
            vertex_key = queue.dequeue()
            for neighbor in self.get_vertex(vertex_key).neighbors:
                if neighbor not in seen:
                    seen[neighbor] = seen[vertex_key] + [neighbor]
                    if neighbor == end:
                        # print(seen[neighbor])
                        return seen[neighbor]
                    queue.enqueue(neighbor)
        return None

    def recursive_dfs(self, start, end, visited=None):
        '''traverses the graph in DFS order from start to end
        returns a boolean expressing whether a path exists or not'''
        if visited is None:
            visited = {start}
        print(start)
        for neighbor in self.get_vertex(start).neighbors:
            if neighbor == end:
                print(neighbor)
                return True
            else:
                visited.add(neighbor)
                return self.recursive_dfs(neighbor, end, visited)

    def dijkstras(self, start, end):
        '''finds the shortest weighted path between a start and an end
        returns the weight of the path'''
        return 'DIJKSTRAS METHOD NOT IMPLEMENTED YET'

    def prims(self):
        edges = []
        smallest_edge = (0, 0, float('inf'))
        sorted_edges = sorted(self.edges, key=lambda tuple: tuple[2])
        # from operator import itemgetter
        # sorted_edges = sorted(self.edges, key=itemgetter(2))
        for edge in sorted_edges:
            if edge[2] < smallest_edge[2]:
                smallest_edge = edge
        edges.append(smallest_edge)

    def shortest_path_directed_acyclic(self, start, end, seen={}):
        if start == end:
            return 0
        min_dist = float('inf')
        if ((start, end)) in seen:
            return seen[(start, end)]
        if self.get_vertex(start).is_pointing_to(end):
            min_dist = self.get_vertex(start).weight_to(end)
        # for every edge in edge list
        for edge in self.edges:
            # if any of the edges points to our end
            if edge[1] == end and edge[0] != start:
                # recursively find the distance from start to end through that midpoint
                dist = self.shortest_path_directed_acyclic(
                    start, edge[0], seen) + self.get_vertex(edge[0]).weight_to(end)
                if dist < min_dist:
                    min_dist = dist
        seen[(start, end)] = min_dist
        return min_dist


if __name__ == '__main__':
    g = ADTGraph()
    g.add_verticies([1, 2, 3, 4, 5])
    g.digraph = False
    g.add_egdes([(1, 2), (2, 3), (3, 4), (4, 5)])
    print([vert for vert in g])

    # shotest_path = g.shortest_path('5', '2')
    # print(shotest_path)
    dfs = g.recursive_dfs(5, 2)
    print(dfs)
    # print(dfs)
