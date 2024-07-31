class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
g = Graph()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node, neighbor = map(int, input("Enter edge (node neighbor): ").split())
    g.add_edge(node, neighbor)
start_node = int(input("Enter the starting node for BFS: "))
print("BFS Traversal starting from node", start_node)
bfs(g.graph, start_node)
