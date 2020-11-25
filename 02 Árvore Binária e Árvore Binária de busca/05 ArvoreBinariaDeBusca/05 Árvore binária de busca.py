class No:
    def __init__(self, chave, proximo=None , anterior=None):
        self.chave = chave
        self.proximo = proximo
        self.anterior = anterior

class ArvoreDeBusca:

    def __init__(self, chave=None):
        if chave != None:
            self.raiz = No(chave)
        else:
            self.raiz = None

    def append(self, chave):
    
        if self.raiz == None:
            self.raiz = No(chave)
            return "0"
        else:
            ponteiro = self.raiz
            contador = 0
            flag = True
            while flag:
                if chave >= ponteiro.chave:
                    contador+=1
                    if ponteiro.proximo == None:
                        ponteiro.proximo = No(chave) 
                        return (str(contador))
                        
                    else:
                        ponteiro = ponteiro.proximo

                elif chave < ponteiro.chave:
                    contador+=1
                    if ponteiro.anterior == None:
                        ponteiro.anterior = No(chave)
                        return (str(contador))
                    else:
                        ponteiro = ponteiro.anterior

    def verificarProfundidade(self, chave, ultimo = False, deletar = False):

        if self.raiz == None:
            return "-1"
        else:
            contador = 0
            ponteiro = self.raiz
            flag = True
            pai = None

            while flag:
                if chave > ponteiro.chave:
                    pai = ponteiro
                    ponteiro = ponteiro.proximo 
                    contador+=1
                    if ponteiro == None:
                        return "-1"
                                    
                elif chave < ponteiro.chave:   

                    pai = ponteiro
                    ponteiro = ponteiro.anterior
                    contador+=1
                    if ponteiro == None:
                        return "-1"
                
                elif chave == ponteiro.chave:

                    if deletar == True:
                        return ponteiro, pai
                    return str(contador)
       
    def altura(self, novoNo):

        if self.raiz == None:
            return "0"

        if novoNo is None:
            novoNo = self.raiz
        esquerda = 0
        direita = 0

        if novoNo != None and novoNo.anterior != None:
            esquerda = self.altura(novoNo.anterior)
        if novoNo != None and novoNo.proximo != None:
            direita = self.altura(novoNo.proximo)
        if direita>esquerda:
            return direita + 1
        return esquerda + 1

    def deletar(self, valorEliminar):
        noAndPai = self.verificarProfundidade(valorEliminar, ultimo = False, deletar = True)
        if noAndPai == "-1":
            return

        no = noAndPai[0]
        pai = noAndPai[1]
        raizPai = self.raiz
        print(no, pai, raizPai)


        #classeDetectada = False
        #if type(no) is No and type(pai) is No:
        #    classeDetectada = True

        #if classeDetectada:
        if no.proximo == None and no.anterior == None:

            if pai == None:
                self.raiz = None

            elif raizPai == None:
                raizPai = None
            else:
                if pai.anterior == no:
                    no = None
                    pai.anterior = None
                elif pai.proximo == no:
                    no = None
                    pai.proximo = None

        elif (no.proximo == None and no.anterior != None) or (no.proximo != None and no.anterior == None):
            if pai == None:
                if no.proximo != None:
                    self.raiz = no.proximo
                elif no.anterior != None:
                    self.raiz = no.anterior

            elif pai.proximo == no:
                if no.proximo != None:
                    pai.proximo = no.proximo
                elif no.anterior != None: 
                    pai.proximo = no.anterior

            elif pai.anterior == no:
                if no.proximo != None:
                    pai.anterior = no.proximo
                elif no.anterior != None: 
                    pai.anterior = no.anterior  

        elif (no.proximo != None and no.anterior != None):
            sucessor = self.encontrarSucessor(no)

            if pai == None:
                self.raiz = sucessor
            else:
                if pai.anterior == no:
                    pai.anterior = sucessor
                else:
                    pai.proximo = sucessor
                
   
    def encontrarSucessor(self, valorApagar):
        paiSucessor = valorApagar
        sucessor = valorApagar
        valorAtual = valorApagar.proximo

        while valorAtual != None:
            paiSucessor = sucessor
            sucessor = valorAtual
            valorAtual = valorAtual.anterior 

        if sucessor != valorApagar.proximo:
            paiSucessor.anterior = sucessor.proximo
            sucessor.proximo = valorApagar.proximo
            
        sucessor.anterior = valorApagar.anterior
        return sucessor

def pegarValores(linha):
    lista = linha.split()
    for x in range(len(lista)):
        lista[x] = int(lista[x])
    return lista

# —————————————————————————————————————————— PRINT ——————————————————————————————————————————         

objeto = ArvoreDeBusca()
opcao = input("Digite: ")
valor = input("Valores: ")
todosValores = pegarValores(valor)

for x in range(len(todosValores)):
    objeto.append(int(todosValores[x]))
print(objeto.altura(None))

while opcao != "END":
    opcao = input()
    if opcao[:3] == "INS":
        print(objeto.append(int(opcao[4:])))
    elif opcao[:3] == "SCH":
        print(objeto.verificarProfundidade(int(opcao[4:])))
    elif opcao[:3] == "DEL":
        print(objeto.verificarProfundidade(int(opcao[4:])))
        objeto.deletar(int(opcao[4:]))
print(objeto.altura(None))

#5, 2, 6, 1, 7, 8, 4, 9, 5, 2, 6, 1, 4
#13
#5 2 6 1 7 8 4 9 5 2 6 1 4

"""
Explicando alguns termos:
01: A entrada inicia com uma linha contendo um inteiro, correspondente à quantidade inicial de nós de uma BST T.



— SCH k : imprime a profundidade do primeiro nó encontrado (nó menos profundo) com valor k. Caso tal nó
não exista, imprime -1.
— INS k : imprime a profundidade da folha com valor k inserida.
— DEL k : imprime a profundidade do nó removido com valor k, se houver. Caso contrário imprime -1. Esse
valor é o mesmo valor que seria impresso por SCH k antes da remoção.
"""