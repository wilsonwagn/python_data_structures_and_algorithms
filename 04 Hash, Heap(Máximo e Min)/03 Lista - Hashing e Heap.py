
class Hash:
    def __init__(self, maximoCadastros):
        self.valorMaximo = 2*maximoCadastros                            
        self.elementos = [[] for x in range(self.valorMaximo)]    
 
    def pegarChave(self, chave, chave2):
        index = self.pegarHash(chave, chave2) 
        for x in self.elementos[index]:
            if x[0] == chave:
                return x[1]
        
    def adicionarPessoas(self, chave, chave2, prioridade, fileira):
        index = self.pegarHash(chave, chave2)
        self.elementos[index].append([chave, chave2, prioridade, fileira])
            
    def transformarStringInteiro(self, chave, chave2):
        total = 1
        for x in range(len(chave)):
            total = total*ord(chave[x])
        total += int(chave2)
        return total

    def pegarHash(self, chave, chave2):
        chave = self.transformarStringInteiro(chave, chave2)
        return chave % self.valorMaximo
    
    def deletar(self, nome, numCadastro):
        indice = self.pegarHash(nome, numCadastro)
        if len(self.elementos) == 1:
            if self.elementos[indice][0] == nome and self.elementos[indice][1] == numCadastro:
                self.elementos[indice] = []
        else:
            contador = 0
            for x in self.elementos[indice]:
                if x[0] == nome and x[1] == numCadastro:
                    flag = True
                    break
                contador+=1
            if flag == True:
                self.elementos[indice].pop(contador)
    
    def retornarFileira(self, nome, numCadastro):
        index = self.pegarHash(nome, numCadastro)
        for x in self.elementos[index]:
            if x[0] == nome and x[1] == int(numCadastro):
                return x
        return False
    
    def atualizar(self, nome, numCadastro, fileira):
        index = self.pegarHash(nome, numCadastro)
        for x in range(len(self.elementos[index])):
            if self.elementos[index][x][0] == nome and self.elementos[index][x][1] == int(numCadastro):
                self.elementos[index][x][3] = fileira
        return False
class heapMax:
    def __init__(self, lista = []):
        self.lista = [None]+lista
        x = (len(lista)//2)
        for i in range(x, 0, -1):
            self.manterHeap(i)
    def manterHeap(self, i):
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
        
    def filhoEsquerda(self, index):
        return 2*index

    def filhoDireita(self, index):
        return 2*index+1

    def paiFilho(self, index):
        return (index)//2

    def inserir(self, nome, numCadastro, prioridade, flag = None):
        if flag == None:  
            self.lista.append([nome, numCadastro, prioridade])
            index = len(self.lista) - 1 
            while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)][2] < prioridade):
                self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
                index = self.paiFilho(index)

    def maximoHeap(self):
        maior = self.lista[1]
        self.lista[1] = self.lista[-1]
        self.lista.pop()
        self.manterHeap(1)
        return maior
    
    def __str__(self):
        printar = "["
        for x in range(len(self.lista)):
            printar += str(self.lista[x])
            printar += ","

        printar = printar[:-1]+"]"
        return printar

    def retornarARaiz(self):
        return self.lista[1][2]

    def tamanhoLista(self):
        if len(self.lista) > 1:
            return True
        return False

    def popHeap(self, index):
        if index == len(self.lista)-1:
            self.lista.pop()
        else:
            self.lista[index] = self.lista[-1]
            self.lista.pop()
            if self.paiFilho(index) > 0:
                if self.lista[index][2] > self.lista[self.paiFilho(index)][2]:
                    self.Blackpink(index)
            else:
                self.manterHeap(index)

    def Blackpink(self, index):
        while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)][2] < self.lista[index][2]):
            self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
            index = self.paiFilho(index)

class heapMin:

    def __init__(self, lista = []):
        self.lista = [None]+lista
        x = (len(lista)//2)
        for i in range(x, 0, -1):
            self.manterHeap(i)
    
    def manterHeap(self, i): 
        esquerda = self.filhoEsquerda(i)
        direita = self.filhoDireita(i)
        maior = i
        if esquerda < len(self.lista) and self.lista[esquerda][2] < self.lista[i][2]:
            maior = esquerda
        if direita < len(self.lista) and self.lista[direita][2] < self.lista[maior][2]:
            maior = direita
        if maior != i:
            self.lista[i], self.lista[maior] = self.lista[maior], self.lista[i]
            self.manterHeap(maior)
        

    def filhoEsquerda(self, index):
        return 2*index

    def filhoDireita(self, index):
        return 2*index+1

    def paiFilho(self, index):
        return (index)//2

    def inserir(self, nome, numCadastro, prioridade, flag = None):

        if flag == None:  
            self.lista.append([nome, numCadastro, prioridade])
            index = len(self.lista) - 1 
            while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)][2] > prioridade):
                self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
                index = self.paiFilho(index)
     
    def maiorPrioridade(self, prioridade):
        for x in range(len(self.lista)):
            if prioridade > self.lista[x][2]:
                return True
        return False

    def prioridadesIguais(self, prioridade):
        cont = 0
        while cont < len(self.lista):
            if self.lista[cont][2] == prioridade:
                pessoaRetirada = self.lista[cont]
                self.lista[cont] = [nome, numCadastro, prioridade]
            cont+=1
            return pessoaRetirada
        
    def minimoHeap(self):
        if self.lista != []:
            menor = self.lista[1]
            self.lista[1] = self.lista[-1]
            self.lista.pop()
            self.manterHeap(1)
            return menor
    
    def retornarARaiz(self):
        return self.lista[1][2]

    def __str__(self):  
        printar = "["
        for x in range(len(self.lista)):
            printar += str(self.lista[x])
            printar += ","
        printar = printar[:-1]+"]"
        return printar

    def getFileiras(self):
        return self.lista

    def retornarFileiraMin(self, nome, numCadastro):
        for w in range(1, len(self.lista)):
            print(self.lista[w])
            if self.lista[w][0] == nome and self.lista[w][1] == numCadastro:
                return self.lista[w]
        return False 
    
    def indiceElemento(self, nome, numCadastro):
        for x in range(1, len(self.lista)):
            if self.lista[x][0] == nome and self.lista[x][1] == numCadastro:
                return x
        return False

    def popHeap(self, index):
        if index == len(self.lista)-1:
            self.lista.pop()
        else:
            self.lista[index] = self.lista[-1]
            self.lista.pop()
            if self.paiFilho(index) > 0:
                if self.lista[index][2] < self.lista[self.paiFilho(index)][2]:
                    self.Blackpink(index)
            else:
                self.manterHeap(index)

    def Blackpink(self, index):
        while (index > 0) and (self.paiFilho(index) > 0) and (self.lista[self.paiFilho(index)][2] > self.lista[index][2]):
            self.lista[index], self.lista[self.paiFilho(index)] = self.lista[self.paiFilho(index)], self.lista[index]
            index = self.paiFilho(index)

comando = input()
qInputs = int(input())

F = int(comando[:1])
Q = int(comando[2:])
maximoCadastros = 2*(F*Q)

pessoasCadastradas = Hash(maximoCadastros)
fileiras = []
filaPessoasSemAssentos = heapMax()
for x in range(F):
    fileiras.append(heapMin())

cadastros = 1
for x in range(qInputs):
    comando = input("").split()
    if comando[0] == "CAD":
        pessoasCadastradas.adicionarPessoas(comando[1], int(cadastros), int(comando[2]), None)
        fileirasOn = False
        for w in range(len(fileiras)):
            if len(fileiras[w].getFileiras()) <= Q:
                fileiras[w].inserir(comando[1], int(cadastros), int(comando[2]))                             
                print(comando[1],"("+str(cadastros)+")","foi alocado(a) na fileira", w+1)
                fileirasOn = True
                pessoasCadastradas.atualizar(comando[1], cadastros, w)
                break
        if fileirasOn == False:
            menor = fileiras[0].retornarARaiz()
            indexFileiraMenorPrioridade = 0
            for w in range(1, len(fileiras)):
                if fileiras[w].retornarARaiz() < menor:
                    menor = fileiras[w].retornarARaiz()
                    indexFileiraMenorPrioridade = w

            if indexFileiraMenorPrioridade != None:
                if menor < int(comando[2]):
                    menor = fileiras[indexFileiraMenorPrioridade].minimoHeap()
                    fileiras[indexFileiraMenorPrioridade].inserir(comando[1], int(cadastros), int(comando[2]))         
                    fileirasOn = True
                    print(comando[1],"("+str(cadastros)+")","foi alocado(a) na fileira", indexFileiraMenorPrioridade+1)
                    filaPessoasSemAssentos.inserir(menor[0], menor[1], menor[2])
                    pessoasCadastradas.atualizar(comando[1], cadastros, indexFileiraMenorPrioridade)
                    pessoasCadastradas.atualizar(menor[0], menor[1], None)
                            
        if fileirasOn == False:
            filaPessoasSemAssentos.inserir(comando[1], int(cadastros), int(comando[2]))
            print(comando[1],"("+str(cadastros)+")","nao foi alocado(a) em nenhuma fileira")
        cadastros+=1
    elif comando[0] == "VER":
        pessoa = pessoasCadastradas.retornarFileira(comando[1], int(comando[2]))
        if pessoa != False:
            if pessoa[3] != None:
                print("Sentado(a) na fileira", pessoa[3]+1)
            else:
                print("Sem assento")
        else:
            print("Inexistente")
    elif comando[0] == "REM":
        pessoa = pessoasCadastradas.retornarFileira(comando[1], int(comando[2]))
        if pessoa == False:
            print("Inexistente")
        else:
            if pessoa[3] != None:
                indice = fileiras[pessoa[3]].indiceElemento(pessoa[0], pessoa[1])
                fileiras[pessoa[3]].popHeap(indice)                                 
                pessoasCadastradas.deletar(comando[1], int(comando[2]))  
                if filaPessoasSemAssentos.tamanhoLista() == True:
                    maior = filaPessoasSemAssentos.maximoHeap()               
                    fileiras[pessoa[3]].inserir(maior[0], maior[1], maior[2])
                    pessoasCadastradas.atualizar(maior[0], maior[1], pessoa[3])
                print("Removido(a)")
            else:
                pessoasCadastradas.deletar(comando[1], int(comando[2])) 
                if filaPessoasSemAssentos.tamanhoLista() == True:
                    filaPessoasSemAssentos.popHeap(indice)
                print("Removido(a)")
