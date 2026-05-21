from numpy import array as ar
from numpy.linalg import norm
from numpy import sum as soma_np

n, e, p = input("Digite três valores separados por espaço: ").split()
n = int(n)
e = int(e)
p = int(p)

lista_cordenadas = [ list(map(float,input().split())) for i in range(n)]

print(f"{lista_cordenadas[0]}")

lista_np = ar(lista_cordenadas)

array_pesos = []
for i in range(e,n+1):
    if i+1> n: break
    distancia = norm(lista_np[i-1]- lista_np[i])
    array_pesos.append(distancia)
print(array_pesos)
array_pesos = soma_np(array_pesos)
print("soma das distancias", array_pesos)
