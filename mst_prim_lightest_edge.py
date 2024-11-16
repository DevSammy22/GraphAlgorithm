def mst_prim(num_nodes, edges):
    S = set()
    F = []
    start_vertex = 0
    S.add(start_vertex)

    while len(S) < num_nodes:
        lightest_edge = None
        minWeight = float("inf")
        for u, v, w in edges:
            if (u in S and v not in S) or (v in S and u not in S):
                if w < minWeight:
                    minWeight = w
                    lightest_edge = u, v, w

        if lightest_edge:
            u, v, w = lightest_edge
            S.add(u)
            S.add(v)
            F.append((u, v, w))

    return F


# Example Usage
num_nodes = 5
edge_list = [
    (0, 1, 2), (0, 3, 6),
    (1, 2, 3), (1, 3, 8), (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

# Find the MST using the greedy algorithm
mst = mst_prim(num_nodes, edge_list)

print(" The edges in the minimum spanning tree: ")
for element in mst:
    print(element)
