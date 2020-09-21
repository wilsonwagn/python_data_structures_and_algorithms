from no import No

# FALTA TERMINAR!
class Pilha:
    def __init__(self):
        self.cabeça = None
        self._tamanho = 0
    
    def append(self, elemento):
        if self.cabeça != None:
            ponteiro = self.cabeça
            while (ponteiro.direita != None):
                ponteiro = ponteiro.direita
            ponteiro.direita = No(elemento)
        else:
            self.cabeça = No(elemento)
        self._tamanho += 1  
    
    def __len__(self):
        return self._tamanho
 
    def __getitem__(self, index):
        ponteiro = self._pegarNo(index)
        if ponteiro != None:
            return ponteiro.dado
        raise IndexError("list index out of range kkkk")
"""
    def __setitem__(self, index, elemento):
        ponteiro = self._pegarNo(index) 
        if ponteiro != None:
            ponteiro.dado = elemento
        else:
            raise IndexError("list index out of range kkkkk")
"""  
    def _pegarNo(self, index): #O primeiro anderline é para o usuário não ter acesso direto a essa função.
        ponteiro = self.cabeça
        for x in range(index):
            if ponteiro != None:
                ponteiro = ponteiro.direita
            else:
                raise IndexError("list index out of range puts...")
        return ponteiro

    def index(self, elemento):
        ponteiro = self.cabeça
        index2 = 0
        while (ponteiro != None):
            if ponteiro.dado == elemento:
                return index2
            ponteiro = ponteiro.direita
            index2 += 1
        raise ValueError(f"{elemento} is not in list kk")

    def insert(self, index, novoElemento):
        novoNo = No(novoElemento)
        if index == 0:
            novoNo.direita = self.cabeça
            self.cabeça = novoNo
        else:
            ponteiro = self._pegarNo(index-1)
            novoNo.direita = ponteiro.direita 
            ponteiro.direita = novoNo
        self._tamanho += 1

    def remove(self, elemento):
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
    
    def __repr__(self):
        printar = "["
        ponteiro = self.cabeça
        while ponteiro != None:
            printar += str(ponteiro.dado)+", "
            ponteiro = ponteiro.direita
        return printar[:-2] + "]"

    def __str__(self):
        return self.__repr__()