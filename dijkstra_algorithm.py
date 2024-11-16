# mine
def dijkstra(n, edges, vertices):
    #n = len(vertices)
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    s = vertices[0] # source node
    S = set() # tracking the visited path
    d = {v : float("inf") for v in vertices} # keeps the distance from source node
    d[s] = 0 # distance to its source
    parent = {v : None for v in vertices} # this helps to reconstruct the path
    mst = []

    while len(S) < len(vertices):
    #while S != set(vertices):
        u = min((v for v in vertices if v not in S), key=lambda x: d[x])
        S.add(u)
        for v, w in graph[u]:
            if v not in S and d[u] + w < d[v]:
                d[v] = d[u] + w
                parent[v] = u

    return d, parent

n = 5
edges = [
    (1, 2, 2),  # Edge from vertex 1 to 2 with weight 2
    (1, 3, 4),  # Edge from vertex 1 to 3 with weight 4
    (2, 3, 1),  # Edge from vertex 2 to 3 with weight 1
    (2, 4, 7),  # Edge from vertex 2 to 4 with weight 7
    (3, 5, 3),  # Edge from vertex 3 to 5 with weight 3
    (4, 5, 1)   # Edge from vertex 4 to 5 with weight 1
]
vertices = [1, 2, 3, 4, 5]

distance, parent = dijkstra(n, edges, vertices)
print("The Shortest distance from the source node: ")
for vertex, distance in distance.items():
    print(f"Vertex {vertex} : {distance}")

print("\nThe predecessor for individual node: ")
for vertex, predecessor in parent.items():
    print(f"Vertex {vertex} : {predecessor}")