# mine
def mst_prim(n, edges, vertices):
    #n = len(vertices)
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    s = vertices[0]
    S = set()
    d = {v : float("inf") for v in vertices}
    d[s] = 0
    parent = {v : None for v in vertices}
    mst = []
    total_cost = 0
    while len(S) < len(vertices):
    #while S != set(vertices):
        u = min((v for v in vertices if v not in S), key=lambda x: d[x])
        S.add(u)
        for v, w in graph[u]:
            if v not in S and w < d[v]:
                d[v] = w
                parent[v] = u

    for u in vertices:
        if parent[u] is not None:
            mst.append((u, parent[u], d[u])) # u is  current vertex, parent[u] parent vertex and du[] = wieght
            total_cost = total_cost + d[u]

    #mst = [(u, parent[u], d[u]) for u in vertices if parent[u] is not None]
    return mst, total_cost

vertices = [1, 2, 3, 4]
edges = [
    (1, 2, 1),  # Edge between vertex 1 and 2 with weight 1
    (1, 3, 4),  # Edge between vertex 1 and 3 with weight 4
    (2, 3, 2),  # Edge between vertex 2 and 3 with weight 2
    (3, 4, 3)   # Edge between vertex 3 and 4 with weight 3
]

n = len(vertices)
mst, cost = mst_prim(n, edges, vertices)
print("minimum spanning tree: ")
for edge in mst:
    print(f"Edge: {edge[0]} <-> {edge[1]}, Weight: {edge[2]}")
print("Total cost: ", cost)