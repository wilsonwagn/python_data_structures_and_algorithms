import random
from ArvoreBinaria import ArvoreBinaria

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
    def __str__(self):
        #Função do print()
        return str(self.dado)
class ArvoreBinariaBusca(ArvoreBinaria):
    def inserir(self, valor):
        parente = None
        auxiliar = self.raiz
        while auxiliar != None:
            parente = auxiliar
            if valor < auxiliar.dado:
                auxiliar = auxiliar.esquerda
            else:
                auxiliar = auxiliar.direita

        #Caso1: Não tenha raiz, ou seja, o valor será a raiz.
        if parente is None:
            self.raiz = No(valor)
        #Caso2: O valor é menor que o pai.
        elif valor < parente.dado:
            parente.esquerda = No(valor)
        else:
            parente.direita = No(valor)
    
    # Função para encontrar:
    def encontrar(self, valor):
        return self._encontrar(valor, self.raiz)
    
    def _encontrar(self, valor, no):
        if no is None:
            return no
        elif no.dado == valor:
            return ArvoreBinariaBusca(no)
        if valor < no.dado:
            return self._encontrar(valor, no.esquerda)
        return self._encontrar(valor, no.direita)
    

    def profundidade(self, valor):
        #Função com objetivo de encontrar a profundidade:
        if self.raiz == None:
            return "Não existe na árvore!"
        else:
            contador = 0
            ponteiro = self.raiz

            flag = True
            while flag:
                if valor > ponteiro.dado:
                    pai = ponteiro
                    ponteiro = ponteiro.direita
                    contador+=1
                    if ponteiro == None:
                        return "Não existe na árvore!"
                elif valor < ponteiro.dado:
                    pai = ponteiro
                    ponteiro = ponteiro.esquerda
                    contador+=1
                    if ponteiro == None:
                        return "Não existe na árvore!"
                elif valor == ponteiro.dado:
                    flag = False
            print(str(contador))
            return

    def menorValor(self, no = None):
        #Função para retornar o menor valor da árvore.
        if no == None:
            no = self.raiz
        while no.esquerda != None:
            no = no.esquerda
        return no.dado

    def maiorValor(self, no = None):
        #Função para retornar o maior valor da árvore.
        if no == None:
            no = self.raiz
        while no.direita != None:
            no = no.direita
        return no.dado
    
    def deletar(self, valor, no = None):
        #3 Casos!
        if no == None:
            no = self.raiz
        if no is None:
            return no

        if valor < no.dado:
            no.esquerda = self.deletar(valor, no.esquerda)
        elif valor > no.dado:
            no.direita = self.deletar(valor, no.direita)
        else:
            #Caso 1: Eliminando a folha + Caso 2: eliminando caso tenha 1 folha.
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            #Caso 3: Eliminando caso tenha duas filhas:
            else:
                substituto = self.menorValor(no.direita) #Pegando o menor valor da sub-arvore a direita.
                no.dado = substituto
                no.direita = self.deletar(substituto, no.direita)
            return no

            

                    

random.seed(77)
def exemplo1():
    valores = random.sample(range(1,1000), 42)
    bst = ArvoreBinariaBusca()
    print("Valores Gerados: ")
    for valor in valores:
        print(valor, end=" ")
        bst.inserir(valor)
    print("\n ")
    return bst

def exemplo2():
    valores = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    bst = ArvoreBinariaBusca()
    for valor in valores:
        bst.inserir(valor)
    return bst


#Testando o buscar:

"""
items = [819, 547, 3, 23465243645243645]
for item in items:
    r = bst.encontrar(item)
    if r is None:
        print(item, "Não encontrado")
    else:
        print(r.raiz.dado, "Encontrado!")
        """

#Testando a função profundidade e deletar:

if __name__ == "__main__":
    bst = exemplo2()
    bst.EmOrdem()
    bst.linhaProfundidade()
    print()
    bst.profundidade(43)
    bst.profundidade(89)
    print("Maior: ", bst.maiorValor())
    print("Menor: ", bst.menorValor())

    bst.profundidade(61)
    bst.deletar(61)
    bst.linhaProfundidade()