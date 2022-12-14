# Python3 Program for Floyd Warshall Algorithm
# This version of the algorithm is from https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
 
# Define infinity as the large enough value. This value will be used for vertices not connected to each other
INF = 99999
 
# Solves all pair shortest path via Floyd Warshall Algorithm

graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]

# Number of vertices in the graph
V = len(graph[0])

def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
 
        # pick all vertices as source one by one
        for i in range(V):
 
            # Pick all vertices as destination for the above picked source
            for j in range(V):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)

def printSolution(dist):
    print("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

floydWarshall(graph)
    