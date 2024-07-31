class Graph:
    def __init__(self, vertices):
        self.vertices, self.graph = vertices, []

    def add_edge(self, u, v, w):
        self.graph += [(u, v, w), (v, u, w)]

def prim(graph):
    vertices, key, parent = graph.vertices, [float('inf')] * graph.vertices, [-1] * graph.vertices
    key[0] = 0

    for _ in range(vertices):
        u = min((i for i in range(vertices) if key[i] < float('inf')), key=key.__getitem__)
        [((v, w), (key.__setitem__(v, w), parent.__setitem__(v, u))) for x, v, w in graph.graph if x == u and w < key[v]]

    print("Minimum Spanning Tree:")
    [print(f"Edge: {parent[i]} - {i}, Weight: {key[i]}") for i in range(1, vertices)]

def main():
    vertices, edges = int(input("Enter the number of vertices: ")), int(input("Enter the number of edges: "))
    graph = Graph(vertices)

    print("Enter edges in the format 'u v weight' (space-separated):")
    [graph.add_edge(*map(int, input().split())) for _ in range(edges)]

    prim(graph)

if __name__ == "__main__":
    main()
