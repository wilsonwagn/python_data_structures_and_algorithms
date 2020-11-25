#Código Python com objetivo apenas de inserir na arvore AVL
# >>> toda vez que inserimos um novo nó, checamos o balanço da árvore.
# >>> toda vez que removemos um nó, checamos o balanço da árvore.

#Classe do nó:
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

#Arvore AVL com apenas inserção!
class ArvoreAVL:
    #Função recursiva para inserir a chave na subárvore.

    #root = no | key = valor
    def inserir(self, no, valor):

        # Passo1: Adicionando normalmente na árvore:
        if not no:
            return No(valor)
        elif valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        else:
            no.direita = self.inserir(no.direita, valor)
        
        # Passo2: Atualizando a altura:
        no.altura = 1 + max(self.getAltura(no.esquerda), self.getAltura(no.direita))
        
        # Passo3: obter o valor do equilíbrio:
        balanco = self.getBalanco(no)

        # Passo4: Balançeamento (Existem 4 casos):
        #Caso1: Esquerda, Esquerda:
        if balanco > 1 and valor < no.esquerda.valor:
            return self.rodarADireita(no)
        
        #Caso2: Direita, Direita:
        if balanco < -1 and valor > no.direita.valor:
            return self.rodarAEsquerda(no)

        #Caso3: Esquerda, Direita:
        if balanco > 1 and valor > no.esquerda.valor:
            no.esquerda = self.rodarAEsquerda(no.esquerda)
            return self.rodarADireita(no)
        #Caso4: Direita, Esquerda:
        if balanco < -1 and valor < no.direita.valor:
            no.direita = self.rodarADireita(no.direita)
            return self.rodarAEsquerda(no)
        return no
        
    def rodarADireita(self, no):
        filho = no.esquerda
        neto = filho.direita

        # Rodando a direita:
        filho.direita = no
        no.esquerda = neto

        # Atualizando a altura:
        no.altura = 1 + max(self.getAltura(no.esquerda), self.getAltura(no.direita))
        filho.altura = 1 + max(self.getAltura(filho.esquerda), self.getAltura(filho.direita))
        
        #Retorna o novo nó
        return filho

    def rodarAEsquerda(self, no):
        filho = no.direita
        neto = filho.esquerda

        #Rodando a Esquerda:
        filho.esquerda = no
        no.direita = neto
        
        # Atualizando a altura:
        no.altura = 1 + max(self.getAltura(no.esquerda), self.getAltura(no.direita))
        filho.altura = 1 + max(self.getAltura(filho.esquerda), self.getAltura(filho.direita))

        #Retorna o novo nó:
        return filho 


    def getAltura(self, no):
        if not no:
            return 0
        return no.altura
    
    def getBalanco(self, no):
        if not no:
            return 0
        return self.getAltura(no.esquerda) - self.getAltura(no.direita)
    
    
    def EmOrdem(self, no):
        #<--, raiz, -->
        if no is None:
            no = self.raiz
            return
        if no.esquerda != None:
            self.EmOrdem(no.esquerda)
        print(no.valor, end=" ")
        if no.direita != None:
            self.EmOrdem(no.direita)

    def preOrdem(self, no):
        if not no:
            return
        print("> ", no.valor, end=" ")
        self.preOrdem(no.esquerda)
        self.preOrdem(no.direita)

# —————————————————————————————————————————— PRINT ——————————————————————————————————————————         

minhaArvoreAVL = ArvoreAVL()
raiz = None
raiz = minhaArvoreAVL.inserir(raiz, 10)
raiz = minhaArvoreAVL.inserir(raiz, 20)
raiz = minhaArvoreAVL.inserir(raiz, 30)
raiz = minhaArvoreAVL.inserir(raiz, 40)
raiz = minhaArvoreAVL.inserir(raiz, 50)
raiz = minhaArvoreAVL.inserir(raiz, 25)

"""A Arvoré ficará da seguinte forma:
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50
                   """


print("Árvore AVL printado em ordem: ")
minhaArvoreAVL.EmOrdem(raiz)
print()
