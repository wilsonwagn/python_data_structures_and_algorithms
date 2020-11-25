class Grafo:
    def __init__ (self, vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(vertices):
            self.grafo.append([0]*(vertices))

        self.antecessores = [-1]*self.vertices
        self.antecessores2 = [-1]*self.vertices

    def adicionarArestas(self, u, v, direcionado):
        if direcionado == False:
            self.grafo[u][v] = 1
            self.grafo[v][u] = 1
        else:
            self.grafo[u][v] = 1
    
    def bfs(self, v):
        visitados = [False] * self.vertices
        for x in range(self.vertices):
            if visitados[x] == False:
                visitados[x] = True
                fila = [x]
                while len(fila) > 0:
                    v = fila[0]
                    for u in range(self.vertices):
                        if self.grafo[v][u] == 1:
                            if visitados[u] == False:
                                visitados[u] = True
                                fila.append(u)
                                self.antecessores2[u] = v
                    fila.pop(0)
        

    def buscaDFS(self, v):
        visitados = [False] * self.vertices
        for x in range(self.vertices):
            if visitados[x] == False:
                self.dfs(x, visitados)

    def dfs(self, u, visitados):
        visitados[u] = True
        for x in range(0, self.vertices):
            if self.grafo[u][x] == 1 and visitados[x] == False:
                self.antecessores[x] = u
                self.dfs(x, visitados)

    def antecessoresDFS(self):
        return self.antecessores

    def antecessoresBFS(self):
        return self.antecessores2


def removerCaracteres(a):
    b = "(), "
    for x in range(0, len(b)):
        a = a.replace(b[x],"-")
    valores = []    
    valor = ""
    for x in range(len(a)):
        if a[x] != "-":
            valor += a[x]
        else:
            if valor != "":
                valores.append(int(valor))
                valor = ""
    return valores

def main():
    d = input()
    if d == "NAO DIRECIONADO":
        arestas = input()
        vertices = input()
        vertices = removerCaracteres(vertices)
    
        grafo = Grafo(max(vertices)+1)
        cont = 0
        while cont < len(vertices):
            grafo.adicionarArestas(vertices[cont], vertices[cont+1], False)
            cont+=2

        grafo.buscaDFS(0)
        print(grafo.antecessoresDFS())
        grafo.bfs(0)
        print(grafo.antecessoresBFS())

    elif d == "DIRECIONADO":
        arestas = input()

        vertices = input()
        vertices = removerCaracteres(vertices)

        grafo = Grafo(max(vertices)+1)
        cont = 0
        while cont < len(vertices):
            grafo.adicionarArestas(vertices[cont], vertices[cont+1], True)
            cont+=2

        grafo.buscaDFS(0)
        print(grafo.antecessoresDFS())
        grafo.bfs(0)
        print(grafo.antecessoresBFS())

if __name__ == '__main__':
    main()

'''
— Exemplos da questão:

NAO DIRECIONADO
6
(0,2) (0,5) (0,4) (2,3) (1,3) (3,5)

DIRECIONADO
6
(0,2) (0,5) (0,4) (2,3) (1,3) (3,5)

——————————————————————————————————————————————————————————————————
NAO DIRECIONADO
8
(5,0) (0,6) (6,7) (7,1) (7,2) (1,2) (1,3) (2,3) (2,4) (3,4)


    (0)---(6)  (1)---(3)
    |      |  / |   /  |
    |      | /  |  /   |
    (5)   (7)——(2)----(4)

[-1, 7, 1, 2, 3, 0, 0, 6]
[-1, 7, 7, 1, 2, 0, 0, 6]
——————————————————————————————————————————————————————————————————

NAO DIRECIONADO
4
(0,3) (0,2) (2,5) (3,5)

——————————————————————————————————————————————————————————————————

NAO DIRECIONADO
7
(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6), (1, 7), (1, 0), (2, 3), (2, 5), (2, 7), (3, 2), (3, 4), (3, 6),  (3, 3), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (5, 7), (6, 2), (6, 3), (6, 4), (6, 1), (6, 7), (7, 6), (7, 3), (7, 2), (7, 1)

——————————————————————————————————————————————————————————————————
NAO DIRECIONADO
4
(0,3) (0,2) (2,5) (3,5) (1,4)

'''



