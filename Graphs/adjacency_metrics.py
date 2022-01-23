class Vertex:
    def __init__(self,node):
        self.id = node
        self.visited = False # mark all nodes as unvisited

    def add_neighbour(self,neighbour,G):
        G.add_edge(self.id,neighbour)

    def get_connections(self,G):
        return G.adjMatrix[self.id]

    def get_vertics_id(self):
        return self.id

    def set_vertics_id(self):
        self.visited = True

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self,numVertices,cost=0):
        self.adjMatrics = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertics = numVertices
        self.vertices = []

        for i in range(0,numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def set_vertex(self,vtx,id):
         if 0 <= vtx<self.numVertics:
             self.vertices[vtx].set_vertics_id(id)


