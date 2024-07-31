class Graph:
    def __init__(self, V):
        self.V, self.graph = V, []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def kruskal(self):
        result, i, edges, parent, rank = [], 0, 0, list(range(self.V)), [0] * self.V
        self.graph.sort(key=lambda x: x[2])
        while edges < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x, y = parent[u], parent[v]
            if x != y:
                edges, result = edges + 1, result + [[u, v, w]]
                parent[x], rank[x] = y, rank[y] + (rank[x] == rank[y])
        return result
V = int(input("Enter the number of vertices: "))
g = Graph(V)
for _ in range(int(input("Enter the number of edges: "))):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    g.add_edge(u - 1, v - 1, w)
print("Edges in the Minimum Spanning Tree:")
for e in g.kruskal():
    print(f"{e[0] + 1} -- {e[1] + 1} == {e[2]}")
