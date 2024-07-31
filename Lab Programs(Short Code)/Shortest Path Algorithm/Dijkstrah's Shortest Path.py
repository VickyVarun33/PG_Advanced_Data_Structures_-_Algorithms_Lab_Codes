import heapq
class Graph:
    def __init__(self):
        self.nodes, self.edges = set(), {}
    def add_node(self, value):
        self.nodes.add(value)
    def add_edge(self, from_node, to_node, weight):
        self.edges.setdefault(from_node, []).append((to_node, weight))
        self.edges.setdefault(to_node, []).append((from_node, weight))  # If the graph is directed, remove this line
def dijkstra(graph, start):
    distances, pq, visited = {node: float('inf') for node in graph.nodes}, [(0, start)], set()
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited: continue
        visited.add(current_node)
        for neighbor, weight in graph.edges.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
# Get user input for the graph
graph, num_vertices = Graph(), int(input("Enter the number of vertices: "))
[graph.add_node(node) for node in range(num_vertices)]
num_edges = int(input("Enter the number of edges: "))
[graph.add_edge(*map(int, input("Enter edge (from to weight): ").split())) for _ in range(num_edges)]
start_node = int(input("Enter the source vertex: "))
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from source vertex:")
[print(f"To {node}: {distance}") for node, distance in shortest_distances.items()]
