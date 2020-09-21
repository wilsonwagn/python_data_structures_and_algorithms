from fila import Fila

# Árvore Binária
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
    def __str__(self):
        #Função do print()
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self, dado = None, no = None):
        if no != None:
            self.raiz = no

        elif dado != None:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None
    
    def EmOrdem(self, no = None):
        #<--, raiz, -->
        if no is None:
            no = self.raiz
        if no.esquerda != None:
            self.EmOrdem(no.esquerda)
        print(no)
        if no.direita != None:
            self.EmOrdem(no.direita)

    def posOrdem(self, no = None):
        #<--, -->, raiz
        if no is None:
            no = self.raiz
        if no.esquerda != None:
            self.posOrdem(no.esquerda)
        if no.direita != None:
            self.posOrdem(no.direita)
        print(no)

    def altura(self, no = None):
        if no is None:
            no = self.raiz
        alturaEsquerda = 0
        alturaDireita = 0

        if no.esquerda != None:
            alturaEsquerda = self.altura(no.esquerda)
        if no.direita != None:
            alturaDireita = self.altura(no.direita)
        
        if alturaDireita > alturaEsquerda:
            return alturaDireita + 1
        return alturaEsquerda + 1

    def linhaProfundidade(self, no = None):
        if no is None:
            no = self.raiz
        
        fila = Fila()
        fila.push(no)
        while len(fila) > 0:
            no = fila.pop()
            if no.esquerda != None:
                fila.push(no.esquerda)
            if no.direita != None:
                fila.push(no.direita)
            print(no, end= " ")



def posOrdemPrint():
    arvore = ArvoreBinaria()

    no1 = No("N")
    no2 = No("I")
    no3 = No("C")
    no4 = No("K")
    no5 = No("I")
    no6 = No("M") 
    no7 = No("I")
    no8 = No("N")
    no9 = No("A")
    no0 = No("J")

    no0.esquerda = no6
    no0.direita = no9
    no2.esquerda = no5
    no2.direita = no4
    no4.direita = no3

    no6.esquerda = no1
    no6.direita = no2

    no8.direita = no7
    no9.esquerda = no8

    arvore.raiz = no0
    return arvore 






