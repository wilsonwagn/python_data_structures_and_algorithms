#Grafo — Matriz de Adjacência.
"""
- Custo é de O(N^2)
- Ideia: associar vértices às linhas e arestas às colunas.
- Grafo não orientado = 0 e 1
- Grafo orientado = 1 se chega no outro vértice, 0 se não há ligação, -1 se chega no vértice padrão.

Representação do grafo de exemplo:

    (A)         (D)
        \     /   |   
          (C)     |
        /     \   |
    (B)         (E)

>>> (A-E == 1-5)

"""

class Grafo:
    #Grafo - Não direcionado
    def __init__ (self, vertices):
        self.vertices = vertices
        self.matriz = []
        for i in range(vertices):
            self.matriz.append([0]*vertices)
            
    def adicionarArestas(self, u, v):
        self.matriz[u - 1][v - 1] = 1
        self.matriz[v - 1][u - 1] = 1

    def mostrarMatriz(self):
        n = 1
        print("     V1    V2    V3    V4    V5")
        print("   ____________________________")
        for x in self.matriz:
            print(f"V{n}| ", end = " ")
            for w in x:
                print(w, end = "     ")
            print("")
            n+=1

    def temLigacao(self, u, v):
        if self.matriz[u-1][v-1] == 1:
            return "Existe essa ligação"
        return "Não tem ligação"

G = Grafo(5)
G.adicionarArestas(1, 3)
G.adicionarArestas(2, 3)
G.adicionarArestas(3, 4)
G.adicionarArestas(3, 5)
G.adicionarArestas(4, 5)
G.mostrarMatriz()
print(G.temLigacao(3, 1))
