# Author: jesus ponce
# GitHub: https://github.com/stronjo
# Date: 2022-03-27

from math import inf

wmat = [[0, 2, 0, 0, 0, 1, 0, 0],
        [2, 0, 2, 2, 4, 0, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 1],
        [0, 2, 0, 0, 4, 3, 0, 0],
        [0, 4, 3, 4, 0, 0, 7, 0],
        [1, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 5, 0, 6],
        [0, 0, 1, 0, 0, 0, 6, 0]]


def find_all(wmat, start, end=-1):
    
    n = len(wmat)

    dist = [inf]*n
    dist[start] = wmat[start][start]  # 0

    spVertex = [False]*n
    parent = [-1]*n

    path = [{}]*n

    for count in range(n-1):
        minix = inf
        u = 0

        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not(spVertex[v]) and wmat[u][v] != 0 and dist[u] + wmat[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + wmat[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]

    return (dist[end], path[end]) if end >= 0 else (dist, path)


def find_shortest_path(wmat, start, end=-1):
    
    return find_all(wmat, start, end)[1]


def find_shortest_distance(wmat, start, end=-1):
   
    return find_all(wmat, start, end)[0]
