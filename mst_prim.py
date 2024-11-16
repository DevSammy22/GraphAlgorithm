#mine
def mst_prim(graph, vertices):
    s = vertices[0]
    S = set()
    d = {v : float("inf") for v in vertices}
    d[s] = 0
    parent = {v : None for v in vertices}
    mst = []

    while len(S) < len(vertices):
    #while S != set(vertices):
        u = min((v for v in vertices if v not in S), key=lambda x: d[x])
        S.add(u)
        for v in vertices:
            if (u, v) in graph and v not in S:
                if graph[(u, v)] < d[v]:
                    d[v] = graph[(u, v)]
                    parent[v] = u

    for u in vertices:
        if parent[u] is not None:
            mst.append((u, parent[u], d[u])) # u is  current vertex, parent[u] parent vertex and du[] = wieght

    #mst = [(u, parent[u], d[u]) for u in vertices if parent[u] is not None]
    return mst

vertices = [1, 2, 3, 4]
edges = {
    (1, 2): 1, (2, 1): 1,
    (1, 3): 4, (3, 1): 4,
    (2, 3): 2, (3, 2): 2,
    (3, 4): 3, (4, 3): 3
}



mst = mst_prim(edges, vertices)
# Print the result
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")