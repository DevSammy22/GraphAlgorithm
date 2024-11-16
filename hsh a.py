# Step 1: Define the Kruskal's Algorithm
def kruskal_algorithm(vertices, edges):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
    :param vertices: List of all vertices in the graph
    :param edges: List of edges in the form (u, v, weight)
    :return: List of edges in the MST
    """
    # Initialize an empty list to store the MST
    mst = []

    # Initialize a separate set for each vertex
    sets = {v: {v} for v in vertices}  # Each vertex is its own set initially

    # Step 2: Sort edges by weight (ascending order)
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight

    # Step 3: Process each edge in sorted order
    for u, v, weight in edges:
        # Find the sets that contain u and v
        set_u = sets[u]
        set_v = sets[v]

        # Step 4: If u and v are not in the same set, include this edge in the MST
        if set_u != set_v:
            mst.append((u, v, weight))  # Add the edge to the MST

            # Merge the two sets
            union_set = set_u | set_v
            for vertex in union_set:
                sets[vertex] = union_set  # Update the set for all vertices in the union

    return mst


# Step 5: Example Usage
vertices = [1, 2, 3, 4]
edges = [
    (1, 2, 1),  # (u, v, weight)
    (1, 3, 4),
    (2, 3, 2),
    (3, 4, 3)
]

# Find the MST
mst = kruskal_algorithm(vertices, edges)

# Print the result
print("Minimum Spanning Tree:", mst)
