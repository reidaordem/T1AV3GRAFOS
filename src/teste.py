import math
from edge import Edge
from edge_weighted_graph import EdgeWeightedGraph
from kruskal_mst import KruskalMST
from uf import UF

n, e, p = map(int, input().split())

lista_coordenadas = [list(map(float, input().split())) for i in range(n)]
lista_cabeada = [list(map(lambda x: int(x)-1, input().split())) for i in range(p)]

graph = EdgeWeightedGraph(n)

for i in range(n):

    if i + 1 >= n:
        break

    ponto_i = lista_coordenadas[i]
    pontos_j = lista_coordenadas[i+1:]

    delta = [[(ponto_j[0]-ponto_i[0]), (ponto_j[1]-ponto_i[1])] for ponto_j in pontos_j]

    distancias = [math.sqrt((par[0]*par[0]) + (par[1]*par[1])) for par in delta]

    if i < e:
        limite = max(0, e - (i + 1))
        for idx in range(limite):
            distancias[idx] = 0

    for par in lista_cabeada:
        if (i == par[0]):
            distancias[par[1]] = 0

    for j, distancia in enumerate(distancias, start=i+1):
        edge = Edge(i, j, float(distancia))
        graph.add_edge(edge)

mst = KruskalMST(graph)
peso_total = 0
for edge in mst.edges():
    peso_total += edge.weight

print("%.6f" % peso_total)