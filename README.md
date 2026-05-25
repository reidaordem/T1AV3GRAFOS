# Trabalho Prático 1 - Unidade 3 

## Problema
Treehouses
link - https://open.kattis.com/problems/treehouses

## Integrantes Grupo C
- Evandro Nobre
- Tiago Goes
- Bruno Cavalcante
- Emanuel Melo

## Linguagem Utilizada
Python

# Execução

## Requisitos
- Python 3.10+

## Comandos

Clone o repositório:

```bash
git clone https://github.com/reidaordem/T1AV3GRAFOS
cd T1AV3GRAFOS/src
```
execute:
```bash
python main.py < ../dados/entrada[1-3].txt
```

# Modelagem do problema como grafo

O problema foi modelado como um grafo ponderado completo e consciste em encontrar o menor custo adicional para conectar todas as casas.

**Vértices** - Cada casa na árvore (treehouse) representa um vértice.

**Aresta** - Cada par de casas pode ser conectado por uma aresta.

**Peso das arestas** - O peso corresponde ao tamanho do cabo (distância euclidiana entre duas casas).


## Algoritmo de Kruskal

Algoritmo encontra uma árvore geradora mínima (MST) usando uma estratégia gulosa (greedy).

A ideia central é:
```text
Sempre escolher a aresta de menor peso possível, desde que ela não forme ciclo.
```

***passo a passo:***
1. Ordenar todas as arestas pelo peso em ordem crescente.
2. Começar com uma floresta:
    - cada vértice é um componente separado.
3. Pecorrer as arestas em ordem crescente:
    - pega a menor aresta disponível;
    - se ela não cria ciclo, adiciona na MST;
    - caso contrário, descarta.
4. Condicao de parada: `V - 1` arestas ná arvore.

# Papel do Union-Find

O problema:
```text 
"Como saber se adicionar uma aresta forma um ciclo?"
```

Para não ter que usar um algoritmo de busca (DFS/BFS), usa-se o Union-Find que mantém grupos de arestas já conectadas. Assim, só precisa verificar se duas arestas pertencem ao mesmo conjunto `(find(u) == find(v))`,caso pertença, a aresta é descartada, uma vez que formaria circulo.

# Variação de MST utilizada

Foi utilizada uma MST com arestas pré-conectadas.

Algumas conexões possuem peso zero antes do algoritmo iniciar.

# Complexidade

- Ordenação das arestas - `O(ElogV)`
- Construção do grafo - `O(n²)`
- Inicialização do Union-Find - `O(V)`
- `find/union` em todas as arestas - `O(E)`
- Total - `O(ElogE)`

## Casos especiais
Casas inicialmente conectadas.
Conexões extras com custo zero.
Distâncias calculadas com números reais.
Grafo completo.
