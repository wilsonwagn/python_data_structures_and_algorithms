class Hash:
    #tabela hash é para guardar as pessoas e sua prioridade, para a lista 3.
    def __init__(self, maximoCadastros):
        self.valorMaximo = 2*maximoCadastros                            #O > valor máximo da questão é 2*F*Q
        self.elementos = [[] for x in range(self.valorMaximo)]          #16 [[][][][]]
 
    def pegarChave(self, chave, chave2):
        index = self.pegarHash(chave, chave2) 
        for x in self.elementos[index]:
            if x[0] == chave:
                return x[1]
        
    def adicionarPessoas(self, chave, chave2, prioridade):
        index = self.pegarHash(chave, chave2)
        self.elementos[index].append([chave, chave2, prioridade, 0])
            
    # >>> Pegar posição da lista:
    def transformarStringInteiro(self, chave, chave2):
        total = 1
        for x in range(len(chave)):
            total = total*ord(chave[x])
        total += chave2
        return total

    def pegarHash(self, chave, chave2):
        chave = self.transformarStringInteiro(chave, chave2)
        return chave % self.valorMaximo
    
    def deletar(self, nome, numCadastro):
        #Deletar apaenas quando for removido do evento.
        indice = self.pegarHash(nome, numCadastro)
        if len(self.elementos[indice]) == 1:
            if self.elementos[indice][0][0] == nome and self.elementos[indice][0][1] == numCadastro:
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