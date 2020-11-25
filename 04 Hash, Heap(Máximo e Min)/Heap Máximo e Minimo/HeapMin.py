
class heapMin:

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
        if esquerda < len(self.lista) and self.lista[esquerda] < self.lista[i]:
            maior = esquerda
        if direita < len(self.lista) and self.lista[direita] < self.lista[maior]:
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

        while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)] > item):
            self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
            index = self.paiFilho(index)
        #print("Index no inserir: ", index)
        self.lista[index] = item

    # ------------------- Outras funções -------------------
    def maximoHeap(self): #extractMax
        #Função que retornar e retira o maior do heap/lista.
        if self.lista != []:
            maior = self.lista[1]
            self.lista[1] = self.lista[-1]
            self.lista.pop()
            #print(self.lista.pop())
            self.manterHeap(1)
            return maior
    
    def __str__(self):
        #Função de print() o heap
        printar = "["
        for x in range(len(self.lista)):
            printar += str(self.lista[x])
            printar += ","

        printar = printar[:-1]+"]"
        return printar

    # ————————————————————————————————— DELETAR ————————————————————————————————— 
    def deletar(self, elemento):
        for x in range(len(self.lista)):
            if self.lista[x] == elemento:
                index = x
                self.popHeap(index, elemento)
                break
        return False
    
    def popHeap(self, index, elemento):
        ponteiro = index*2
        self.lista[index] = self.lista[-1]
        self.lista.pop()

        if self.lista[ponteiro] < self.paiFilho(index):
            self.Blackpink(index)
        else:
            self.manterHeap(index)

    def Blackpink(self, index):
        while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)] > item):
            self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
            index = self.paiFilho(index)

lista = [1, 5, 6, 9, 11, 8, 15, 17, 21]
if __name__ == "__main__":
    tabelaHeap = heapMin(lista)
    print("> ", tabelaHeap)
    tabelaHeap.deletar(5)
    print("> ", tabelaHeap)
