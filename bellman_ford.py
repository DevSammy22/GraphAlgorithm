def bellman_ford(n, edges, s):
    F = {i : float("inf") for i in range(1, n+1)} #distance
    F[s] = 0

    for length in range(n -1):
        updated = False
        for u, v, w in edges:
            if F[u] + w < F[v]:
                F[v] = F[u] + w
                updated = True

        if not updated:
            break
    for u, v, w in edges:
        if F[u] + w < F[v]:
            F[v] = F[u] + w
            return "negative cycle exists", None

    return F


# Example Usage
n = 5  # Number of vertices
edges = [
    (1, 2, 6),  # Edge from vertex 1 to 2 with weight 6
    (1, 3, 7),  # Edge from vertex 1 to 3 with weight 7
    (2, 4, 5),  # Edge from vertex 2 to 4 with weight 5
    (3, 4, -3), # Edge from vertex 3 to 4 with weight -3
    (4, 5, 2)   # Edge from vertex 4 to 5 with weight 2
]
source = 1  # Starting vertex

result = bellman_ford(n, edges, source)

# Output results


if result[1] is None:
    print(result[0])
else:
    print("Shortest distances from source:", result)
