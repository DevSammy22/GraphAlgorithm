def floyd_warshall(n, graph):
    distance = [[float("inf")] * n for _ in range(n)]

    for u, v, w in graph:
        distance[u][v] = w
    for i in range(n):
        distance[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]


    return distance

# Example Usage
n = 4  # Number of vertices
edges = [
    (0, 1, 3),  # Edge from vertex 0 to 1 with weight 3
    (0, 2, 10), # Edge from vertex 0 to 2 with weight 10
    (1, 2, 1),  # Edge from vertex 1 to 2 with weight 1
    (2, 3, 2),  # Edge from vertex 2 to 3 with weight 2
    (3, 0, 7)   # Edge from vertex 3 to 0 with weight 7
]

result = floyd_warshall(n, edges)
print("The shortest path matrix: ")
for row in result:
    print(row)
