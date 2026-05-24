import math

from edge import Edge
from edge_weighted_graph import EdgeWeightedGraph
from prim_mst import PrimMST

n, e, p = input("").split()
n = int(n)
e = int(e)
p = int(p)

lista_cordenadas = [ list(map(float,input().split())) for i in range(n)]



matriz_pesos = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if i<e and j<e:
            distancia = 0
        else:
            distancia = math.dist(lista_cordenadas[i], lista_cordenadas[j])
        matriz_pesos[i][j] = distancia
        matriz_pesos[j][i] = distancia
for i in range(p):
    v, w = input("").split()
    v = int(v)-1
    w = int(w)-1
    matriz_pesos[v][w] = 0
    matriz_pesos[w][v] = 0


graph = EdgeWeightedGraph(n)
for i in range(n):
    for j in range(i+1, n):
        if i != j:
            edge = Edge(i, j, float(matriz_pesos[i][j]))
            graph.add_edge(edge)
mst = PrimMST(graph)
print("%.6f" % mst.weight())

bp=1
