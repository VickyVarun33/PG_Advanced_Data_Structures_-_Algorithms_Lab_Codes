class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

def kruskal(graph):
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    parent = {i: i for i in range(1, graph.vertices + 1)}
    result = []

    def find_set(i):
        if parent[i] == i:
            return i
        return find_set(parent[i])

    def union_set(u, v):
        parent[find_set(u)] = find_set(v)

    for _ in range(graph.vertices - 1):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        graph.add_edge(u, v, w)

    for edge in graph.graph:
        u, v, w = edge
        u_set, v_set = find_set(u), find_set(v)

        if u_set != v_set:
            result.append([u, v, w])
            union_set(u_set, v_set)

    return result

# Example Usage:
num_vertices = int(input("Enter the number of vertices: "))
g = Graph(num_vertices)

minimum_spanning_tree = kruskal(g)

print("\nMinimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}  Weight: {edge[2]}")
