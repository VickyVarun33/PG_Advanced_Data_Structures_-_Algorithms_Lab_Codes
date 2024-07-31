class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)
g = Graph()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node, neighbor = map(int, input("Enter edge (node neighbor): ").split())
    g.add_edge(node, neighbor)
start_node = int(input("Enter the starting node for DFS: "))
print("DFS Traversal starting from node", start_node)
dfs(g.graph, start_node, set())
