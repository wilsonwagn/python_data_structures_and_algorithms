
class Graph: 
    def __init__(self, num_of_vertices): 
        self.vertices = num_of_vertices 
        self.adjacency_matrix = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.edges = [] 

    def fill_edges(self):
        for x in range(self.vertices): 
            for y in range(self.vertices):
                if self.adjacency_matrix[x][y] != 0 and (x,y,self.adjacency_matrix[x][y]) not in self.edges: 
                    self.edges.append((x,y,self.adjacency_matrix[x][y]))

    def find(self, parent, i):
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, vertex_1, vertex_2): 
        super_parent_1 = self.find(parent, vertex_1) 
        super_parent_2 = self.find(parent, vertex_2) 
  
        if rank[super_parent_1] < rank[super_parent_2]: 
            parent[super_parent_1] = super_parent_2 
        elif rank[super_parent_1] > rank[super_parent_2]: 
            parent[super_parent_2] = super_parent_1 
        else : 
            parent[super_parent_2] = super_parent_1 
            rank[super_parent_1] += 1

    def kruskals_mst(self): 
        out = []
        i = 0 
        self.edges =  sorted(self.edges,key=lambda e: e[2])
        parent = [] ; rank = []

        for node in range(self.vertices): 
            parent.append(node) 
            rank.append(0) 
        while len(out) < self.vertices -1:
            vertex_1, vertex_2, weight =  self.edges[i] 
            i = i + 1
            root_of_vertex_1 = self.find(parent, vertex_1) 
            root_of_vertex_2 = self.find(parent ,vertex_2)  

            if root_of_vertex_1 != root_of_vertex_2: 
                out.append([vertex_1,vertex_2,weight]) 
                self.union(parent, rank, vertex_1, vertex_2)  
        return out

def main():
    flag = True
    cont = 0
    centrosValores = []
    centrosPesos = []
    while flag:
        try:    
            valores = input()
            valores = valores.split(", ")
            if valores[0] != "":
                if valores[0] not in centrosValores:
                    centrosValores.append(valores[0])
                    centrosValores.append(cont)
                    cont+=1
                if valores[1] not in centrosValores:
                    centrosValores.append(valores[1])
                    centrosValores.append(cont)
                    cont+=1
                centrosPesos.append([valores[0], valores[1], int(valores[2])])
            else:
                break
        except:
            flag = False

    matriz = []
    for x in range(int(len(centrosValores)/2)):
        a = int(len(centrosValores)/2)
        matriz.append([0]*a)

    for x in range(len(centrosPesos)):
        
        for centro in centrosValores:
            valor = centrosPesos[x] 
            index1 = centrosValores.index(valor[0])
            index2 = centrosValores.index(valor[1])
            index1 = centrosValores[index1+1]
            index2 = centrosValores[index2+1]
            matriz[index1][index2] = valor[2]

    graph = Graph(int(len(centrosValores)/2)) 
    graph.adjacency_matrix = matriz
    graph.fill_edges()
    arvoreMinima = graph.kruskals_mst()
    resposta = 0
    for x in arvoreMinima:
        resposta += x[2]
    print(resposta)
if __name__ == '__main__':
    main()
