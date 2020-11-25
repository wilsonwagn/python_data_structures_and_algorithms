
class heapMax:

    def __init__(self, lista = []):
        self.lista = [None]+lista
        x = (len(lista)//2)
        for i in range(x, 0, -1):
            self.manterHeap(i)
    
    #  ------------------- Função com objetivo de manter o heap máximo:  ------------------- 

    def manterHeap(self, i): #HeapFy
        esquerda = self.filhoEsquerda(i)
        direita = self.filhoDireita(i)
        maior = i
        if esquerda < len(self.lista) and self.lista[esquerda] > self.lista[i]:
            maior = esquerda
        if direita < len(self.lista) and self.lista[direita] > self.lista[maior]:
            maior = direita
        if maior != i:
            self.lista[i], self.lista[maior] = self.lista[maior], self.lista[i]
            self.manterHeap(maior)
        
    # ------------------- Funções para verificar os filhos e pai -------------------

    def filhoEsquerda(self, index):
        return 2*index

    def filhoDireita(self, index):
        return 2*index+1

    def paiFilho(self, index):
        return (index)//2

    # ------------------- Inserção -------------------

    def inserir(self, item):
        #Função com objetivo de inserir no Heap:
        self.lista.append(item)
        index = len(self.lista)-1
        print("LISTA: ", self.lista)

        while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)] < item):
            self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
            index = self.paiFilho(index)
        #print("Index no inserir: ", index)
        self.lista[index] = item

    # ------------------- Outras funções -------------------
    def maximoHeap(self):
        #Função que retornar e retira o maior do heap/lista.
        maior = self.lista[0]
        self.lista[0] = self.lista[-1]
        self.lista.pop()
        self.manterHeap(0)
        return maior
    
    def __str__(self):
        #Função de print() o heap
        printar = "["
        for x in range(len(self.lista)):
            printar += str(self.lista[x])
            printar += ","

        printar = printar[:-1]+"]"
        return printar

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
if __name__ == "__main__":
    a = []
    a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for v in range(len(lista)):
        i = (2*lista[v]*lista[v]) - (10*lista[v])
        a.append(i)
    tabelaHeap = heapMax(a)
    tabelaHeap2 = heapMax(a2)
    #tabelaHeap.maximoHeap()
    print("1º: ", tabelaHeap2)
    print("2º: ", tabelaHeap)

