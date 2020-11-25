
"""
BUSCA EM PROFUNDIDADE:

– Determinar se há ciclos no grafo
– Identificar os componentes conexos do grafo
– Determinar a ordem de execução de tarefas onde
existe interdependência.
— Se utiliza da estrutura pilha.

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

    def dfs(self, u):
        #Busca em profundidade.
        #u = vertice que será iniciado. 
        self.visitados[u - 1] = True
        print(u, "visitado")
        for x in range(1, self.vertices+1):
            if self.grafo[u-1][x-1] == 1 and self.visitados[x-1] == False:
                self.dfs(x)

GrafoBuscaProfundidade = Grafo(5)
GrafoBuscaProfundidade.adicionarArestas(1, 3)
GrafoBuscaProfundidade.adicionarArestas(2, 3)
GrafoBuscaProfundidade.adicionarArestas(3, 4)
GrafoBuscaProfundidade.adicionarArestas(3, 5)
GrafoBuscaProfundidade.adicionarArestas(4, 5)
GrafoBuscaProfundidade.dfs(1)

#EXEMPLO DA LISTA 5
"""
print("\nLISTA 5: ")
GrafoBuscaProfundidade = Grafo(6)
GrafoBuscaProfundidade.adicionarArestas(0, 2)
GrafoBuscaProfundidade.adicionarArestas(0, 5)
GrafoBuscaProfundidade.adicionarArestas(0, 4)
GrafoBuscaProfundidade.adicionarArestas(2, 3)
GrafoBuscaProfundidade.adicionarArestas(1, 3)
GrafoBuscaProfundidade.adicionarArestas(3, 5)
GrafoBuscaProfundidade.dfs(0)
"""