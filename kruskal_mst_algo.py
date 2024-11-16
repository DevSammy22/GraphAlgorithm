#mine
def root_node(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node
def mst_kruskal(num_nodes, edges):
    mst = [] # F in psuedocode
    parent = [v for v in range(num_nodes)]
    edges.sort(key=lambda edge:edge[2])

    for u, v, w in edges:
        root_u = root_node(parent, u)
        root_v = root_node(parent, v)
        if root_u != root_v:
            mst.append((u, v, w))
            parent[root_u] = root_v

    return mst


# Example Usage
num_nodes = 5

# Edges of the graph (u, v, weight)
edges = [
    (0, 1, 1),  # Edge between node 0 and 1 with weight 1
    (0, 2, 2),  # Edge between node 0 and 2 with weight 2
    (1, 2, 2),  # Edge between node 1 and 2 with weight 2
    (1, 3, 1),  # Edge between node 1 and 3 with weight 1
    (3, 4, 3),  # Edge between node 3 and 4 with weight 3
]

# Find the MST
result = mst_kruskal(num_nodes, edges)
print("The minimum spanning tree is: ")
for u, v, w in result:
    print(u, v, w)
'''
#for element in result:
    #print(element)
'''
