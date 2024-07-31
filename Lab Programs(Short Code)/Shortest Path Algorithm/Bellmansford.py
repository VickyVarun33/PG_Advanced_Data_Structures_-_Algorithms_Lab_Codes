def bellman_ford(graph, source):
    n = len(graph)
    distances, predecessors = {v: float('inf') for v in range(n)}, {v: None for v in range(n)}
    distances[source] = 0
    for _ in range(n - 1):
        for v in graph:
            for u, w in graph[v]:
                if distances[v] + w < distances[u]:
                    distances[u], predecessors[u] = distances[v] + w, v
    for v in graph:
        for u, w in graph[v]:
            if distances[v] + w < distances[u]:
                raise ValueError("Graph contains a negative cycle")
    return distances, predecessors
def main():
    n, m = map(int, input("Enter the number of vertices and edges: ").split())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        start, end, weight = map(int, input("Enter edge (start end weight): ").split())
        graph[start].append((end, weight))
    source_vertex = int(input("Enter the source vertex: "))
    try:
        distances, predecessors = bellman_ford(graph, source_vertex)
        print("\nShortest distances from the source vertex:")
        for v, d in distances.items():
            print(f"To {v}: {d}")
        print("\nPredecessors:")
        for v, p in predecessors.items():
            print(f"{v}: {p}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
