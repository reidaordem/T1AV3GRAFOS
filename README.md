# Treehouses

## Problema
Treehouses

## Link do Problema
https://open.kattis.com/problems/treehouses

## Integrantes
- Evandro Nobre
- Tiago Goes
- Bruno Cavalcante
- Emanuel Melo

## Linguagem Utilizada
Python

---

# Como executar

## Requisitos
- Python 3.10+

## Executar

Clone o repositório:

```bash
git clone https://github.com/reidaordem/T1AV3GRAFOS
cd T1AV3GRAFOS/src
```
execute:
```bash
python main.py
```
Insira os dados no formato exigido pelo problema.


# Modelagem do problema como grafo

O problema foi modelado como um grafo ponderado completo.

## Vértices

Cada casa na árvore (treehouse) representa um vértice.

## Arestas

Cada par de casas pode ser conectado por uma aresta.

## Peso das arestas

O peso corresponde à distância euclidiana entre duas casas.

# Casos especiais:

As primeiras e casas já estão conectadas → custo 0.
As conexões adicionais fornecidas na entrada também possuem custo 0.

O objetivo é encontrar o menor custo adicional necessário para conectar todas as casas

## Algoritmo utilizado

Foi utilizado o algoritmo de Prim (Minimum Spanning Tree - MST).

A estratégia consiste em:

Construir o grafo com todas as possíveis conexões.
Aplicar custo 0 às conexões já existentes.
Executar Prim para selecionar as arestas de menor custo.
Somar os pesos das arestas escolhidas.

# Papel da fila de prioridade

Foi utilizada uma fila de prioridade mínima indexada (IndexMinPQ).

Funções principais:

selecionar rapidamente o próximo vértice mais barato;
atualizar distâncias quando uma conexão melhor é encontrada;
reduzir o custo total do algoritmo.

# Variação de MST utilizada

Foi utilizada uma MST com arestas pré-conectadas.

Algumas conexões possuem peso zero antes do algoritmo iniciar.

# Complexidade
Tempo

Construção do grafo:

O(n²)

Prim com fila de prioridade:

O(E log V)

Como o grafo é completo:

O(n² log n)

Memória

Matriz de pesos:

O(n²)

Estruturas auxiliares:

O(n)

## Casos especiais
Casas inicialmente conectadas.
Conexões extras com custo zero.
Distâncias calculadas com números reais.
Grafo completo.
