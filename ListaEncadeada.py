''' 
         head           Segundo           terceiro
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.direita = None

class ListaEncadeada:
    #Iniciamos o init com a cabeça sendo None, para a lista poder começar vazia.
    def __init__(self):
        self.cabeça = None
        self._tamanho = 0 #O primeiro anderline é para o usuário não ter acesso direto, apenas quando utilizar a função len()
    
    def append(self, elemento):
        #Se for verdade que a cabeça já tem elementos, então vamos adicionar um novo valor.
        if self.cabeça != None:
            # Inserção já com elementos na lista:
            ponteiro = self.cabeça
            while (ponteiro.direita != None):  #Utilizamos o while porque não sabemos a quantidade de elementos da lista.
                ponteiro = ponteiro.direita
            ponteiro.direita = No(elemento)
        else:
            # Primeira inserção:
            self.cabeça = No(elemento)
        self._tamanho += 1  
    
    def __len__(self):
        return self._tamanho
    
    def __getitem__(self, index):
        # Encontrar o elemento através dos colchetes. W = lista[0]
        ponteiro = self._pegarNo(index)
        if ponteiro != None:
            return ponteiro.dado
        else:
            print("list index out of range")

    def __setitem__(self, index, elemento):
        # Adicionar novo elemento de acordo com index. Lista[0] == 5

        ponteiro = self._pegarNo(index) 
        if ponteiro != None:
            ponteiro.dado = elemento
        else:
            raise IndexError("list index out of range kkkkk")
    
    def _pegarNo(self, index): #O primeiro anderline é para o usuário não ter acesso direto a essa função.
        #Essa função tem como objetivo apenas pegar exatamente a posição do index.
        ponteiro = self.cabeça
        for x in range(index):
            if ponteiro != None:
                ponteiro = ponteiro.direita
            else:
                raise IndexError("list index out of range puts...")
        return ponteiro

    def index(self, elemento):
        # Igual a função nativa index, retornar o indice do elemento da lista.

        ponteiro = self.cabeça
        index2 = 0
        while (ponteiro != None):
            if ponteiro.dado == elemento:
                return index2
            ponteiro = ponteiro.direita
            index2 += 1
        raise ValueError(f"{elemento} is not in list kk")

    def insert(self, index, novoElemento):
        #Aqui temos 2 casos:
        #1 caso: usuário queira inserir no inicio da lista, ou seja, cabeça.
        #2 caso: usuário queira inserir apartir da 2 posição em diante.

        novoNo = No(novoElemento)
        if index == 0:
            #Aqui também tratamos, caso a lista seja vazia.
            novoNo.direita = self.cabeça
            self.cabeça = novoNo
        else:
            ponteiro = self._pegarNo(index-1)
            novoNo.direita = ponteiro.direita 
            ponteiro.direita = novoNo
        self._tamanho += 1

    def remove(self, elemento):
        #Caso 1: Caso o primeiro elemento a ser eliminado, seja a cabeça
        if self.cabeça == None:
            raise ValueError(f"{elemento} is not in list kk")
        elif self.cabeça.dado == elemento:
            self.cabeça = self.cabeça.direita
            self._tamanho -= 1
            return True
        else:
            antecessor = self.cabeça
            ponteiro = self.cabeça.direita
            while (ponteiro != None):
                if ponteiro.dado == elemento:
                    antecessor.direita = ponteiro.direita
                    ponteiro.direita = None

                antecessor = ponteiro
                ponteiro = ponteiro.direita
            self._tamanho -= 1
            return True
        raise ValueError(f"{elemento} is not in list kk")
    
    #Funções de print:
    def __repr__(self):
        #Função de printar apenas citando a variavel.
        printar = "["
        ponteiro = self.cabeça
        while ponteiro != None:
            printar += str(ponteiro.dado)+", "
            ponteiro = ponteiro.direita
        return printar[:-2] + "]"

    def __str__(self):
        #Função do print()
        return self.__repr__()

if __name__ == "__main__":
    
    lista = ListaEncadeada()
    lista.append(7)
    lista.append(80) 
    lista.append(56)
    lista.append(32)
    lista.append(17)
    print(lista)
    lista.insert(0, 22)
    lista.insert(3, 800)

    lista[0]
    lista[1]
    lista[2]
    lista[3]
    lista[4]
    lista[5]
    lista[6]
    lista.remove(800)
    lista[3]
    lista[4]
    lista[5]
    lista[6]