#listas de adjacência é feita com o auxílio de listas encadeadas
"""
Representação do grafo de exemplo:

    (A)         (D)
        \     /   |   
          (C)     |
        /     \   |
    (B)         (E)

>>> (A-E == 1-5)

"""
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = []
        for x in range(vertices):
            self.lista.append([])
    
    def adicionarArestas(self, u, v):
        self.lista[u-1].append(v-1)

    def mostrarLista(self):
        for x in range(self.vertices):
            print(x+1, end = " ")
            for w in self.lista[x]:
                print(w+1, end = " ")
            print()

G = Grafo(5)
G.adicionarArestas(1, 3)
G.adicionarArestas(2, 3)
G.adicionarArestas(3, 4)
G.adicionarArestas(3, 5)
G.adicionarArestas(4, 5)
G.mostrarLista()
