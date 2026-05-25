import math
from edge import Edge
from uf import UF

n, e, p = map(int, input().split())

lista_cordenadas = [list(map(float, input().split())) for i in range(n)]

edges = []

uf = UF(n)

for i in range(1, e):
    uf.union(0, i)

for i in range(p):
    v, w = input("").split()
    v = int(v) - 1
    w = int(w) - 1
    uf.union(v, w)

for i in range(n):
    for j in range(i + 1, n):
        if not uf.connected(i, j):
            distancia = math.dist(lista_cordenadas[i], lista_cordenadas[j])
            edges.append(Edge(i, j, distancia))

edges.sort()

total_weight = 0
edges_used = 0

for edge in edges:
    v = edge.either()
    w = edge.other(v)
    if not uf.connected(v, w):
        uf.union(v, w)
        total_weight += edge.weight
        edges_used += 1
        if edges_used == n - 1:  
            break

print("%.6f" % total_weight)
