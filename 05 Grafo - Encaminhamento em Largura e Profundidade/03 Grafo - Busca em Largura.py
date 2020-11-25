"""
BUSCA EM LARGURA:

busca em largura ela sempre retorna o caminho mais curto
desde a origem a qualquer outro vértice no mesmo componente conexo.

— Se utiliza da estrutura fila.

|E| = Quantidade de arestas / |V| = Quantidade de vertices:

— Complexidade de tempo é O(|E|+|V|)
— Complexidade de espaço é O(|V|)

Representação do grafo de exemplo:

    (A)         (D)
        \     /   |   
          (C)     |
        /     \   |
    (B)         (E)

>>> (A-E == 1-5)

"""

class Grafo:
    #Grafo - Busca de profundidade
    def __init__ (self, vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(vertices):
            self.grafo.append([0]*vertices)
        self.visitados = [False] * vertices
            
    def adicionarArestas(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def mostrarGrafo(self):
        for x in self.grafo:
            for w in x:
                print(w, end = "     ")
            print("")

    def temLigacao(self, u, v):
        if self.grafo[u-1][v-1] == 1:
            return "Existe essa ligação"
        return "Não tem ligação"

    def bfs(self, v):
        #Busca em largura:
        #v = onde o vertice irá começar.
        self.visitados[v-1] = True
        fila = [v-1]
        print(v, "visitado")
        while len(fila) > 0:
            v = fila[0]
            for u in range(self.vertices):
                #Verificando se os visinhos foram visitados.
                if self.grafo[v][u] == 1:
                    if self.visitados[u] == False:
                        self.visitados[u] = True
                        fila.append(u)
                        print(f"{u+1} visitado")

            #Removendo o vetor da fila:
            fila.pop(0)

GrafoBuscaProfundidade = Grafo(5)
GrafoBuscaProfundidade.adicionarArestas(1, 3)
GrafoBuscaProfundidade.adicionarArestas(2, 3)
GrafoBuscaProfundidade.adicionarArestas(3, 4)
GrafoBuscaProfundidade.adicionarArestas(3, 5)
GrafoBuscaProfundidade.adicionarArestas(4, 5)
GrafoBuscaProfundidade.bfs(1)
print("_")

GrafoBuscaProfundidade = Grafo(6)
GrafoBuscaProfundidade.adicionarArestas(0, 2)
GrafoBuscaProfundidade.adicionarArestas(0, 5)
GrafoBuscaProfundidade.adicionarArestas(0, 4)
GrafoBuscaProfundidade.adicionarArestas(2, 3)
GrafoBuscaProfundidade.adicionarArestas(1, 3)
GrafoBuscaProfundidade.adicionarArestas(3, 5)
GrafoBuscaProfundidade.bfs(0)
