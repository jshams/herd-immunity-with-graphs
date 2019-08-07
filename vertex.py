#!python


class Vertex(object):
    def __init__(self, data: str):
        self.data = data
        self.neighbors = dict()

    def points_to(self, neighbor_key, weight=1):
        '''Adds a edge from this vertex to the given neighboring vertex with the given weight'''
        self.neighbors[neighbor_key] = weight

    def is_pointing_to(self, key: str):
        '''Returns a boolean indicating whether the vertex is pointing to another item'''
        return key in self.neighbors

    def weight_to(self, neighbor_key):
        if self.is_pointing_to(neighbor_key):
            return self.neighbors[neighbor_key]

    def __hash__(self):
        return hash(self.data)


# {'A': {'B': 53, 'C': 12}, 'C': {'A': 12}, 'B': {}}
# {'A': Vertex(data='A', neighbors={'B': 53, 'C': 12}), ...}
