def mst_kruskal_algo(vertices, edges):
    mst = []
    sets = {v : {v} for v in vertices}
    edges.sort(key=lambda edge:edge[2])

    for (u, v, w) in edges:
        set_u = set[u]
        set_v = set[v]

        if set_u != set_v:
            mst.append((u, v, w))
            union_set = set_u | set_v

            for vertex in union_set:
                sets[vertex] = union_set

    return mst

# Example Usage
vertices = [1, 2, 3, 4]
edges = [
    (1, 2, 1),  # (u, v, weight)
    (1, 3, 4),
    (2, 3, 2),
    (3, 4, 3)
]

result = mst_kruskal_algo(vertices, edges)
print("The minimum spanning tree is: ", result)