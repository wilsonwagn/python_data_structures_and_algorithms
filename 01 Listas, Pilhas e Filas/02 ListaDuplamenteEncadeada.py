class No:
    def __init__(self, valor = None, proximo = None, anterior = None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior
    
    def __str__(self):
        return str(self.valor)

class duplaEncadeada:

    def __init__(self, valor = None):
        self.cabeça = None # Cabeça é o primeiro;
        self.rabo = None # Rabo é último elemento
        self.tamanho = 0


        if valor != None:
            self.cabeça = No(valor)
            self.rabo = No(valor)
            self.tamanho = 1

    def pegarElementoDeAcordoIndex(self, index):
        #Essa função vai retorar o elemento de acordo com o index, o elemento será um nó.

        cont = 0
        if self.tamanho == 0:
            return
        else:
            elemento = self.cabeça                  #Aqui recebemos o valor da cabeça do Init.
            while elemento != None:                 #Enquanto existir números na lista:
                if cont == index:
                    return elemento
                else:
                    elemento = elemento.proximo
                    cont+=1

    def append(self, valor, index = None):
        novoNo = No(valor)
        if index == None: 
            if self.tamanho == 0:
                self.cabeça = novoNo
                self.rabo = novoNo
                self.tamanho+=1
            
            else:
                self.rabo.proximo = novoNo
                novoNo.anterior = self.rabo
                self.rabo = novoNo 
                self.tamanho+=1
        
        #Aqui iremos adicionar de acordo com a posição.
        else:
            if self.tamanho == 0:
                self.cabeça = novoNo
                self.rabo = novoNo
                self.tamanho+=1
            else:
                """
                Exemplo: [10, 20, 30]
                Eu quero adicionar 50 na posição 1.
                """
                antigoIndice = self.pegarElementoDeAcordoIndex(index) #50     #20    #Aqui estou pegando o valor 20, pois estou pegando de acordo com o index. [10, 20, 30]
                novoNo.anterior = antigoIndice.anterior               #5     #[10*,50] | *Onde teve alteração.
                antigoIndice.anterior = novoNo                          #20.anterior = novo [10, 50*, 20, 30] | Aqui ele não substitui, apenas adiciona.
                novoNo.proximo = antigoIndice                           #[10,50,*,30] e depois fica assim [10, 50, 20, 30]
                cabeça = antigoIndice.anterior.anterior
                cabeça.proximo = novoNo
                self.tamanho+=1

    #Funções de print:
    def __repr__(self):
        #Função de printar apenas citando a variavel.
        printar = "["
        ponteiro = self.cabeça
        while ponteiro != None:
            printar += str(ponteiro.valor)+", "
            ponteiro = ponteiro.proximo
        return printar[:-2] + "]"

# —————————————————————————————————————————— PRINT ——————————————————————————————————————————         
lista = duplaEncadeada()
lista.append(5)
lista.append(9)
lista.append(10)
print(">", lista)
lista.append(9999, 1)
print(">>", lista)



        
