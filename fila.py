# Nó para alocação de uma Fila
class No:
    def __init__(self, dado):
        self.dado = dado
        self.direita = None

# Classe que define uma Fila
class Fila:
    def __init__(self):
        self.primeiroFila = None
        self.ultimoFila = None
        self._tamanho = 0

    # inserir na fila
    def push(self, elem):
        """Insere um elemento na fila"""
        no = No(elem)
        if self.ultimoFila is None:
            self.ultimoFila = no
        else:
            self.ultimoFila.direita = no
            self.ultimoFila = no

        if self.primeiroFila is None:
            self.primeiroFila = no

        self._tamanho += 1

    # remover da fila
    def pop(self):
        """Remove o elemento do topo da pilha""" 
        if self._tamanho > 0:
            elem = self.primeiroFila.dado
            self.primeiroFila = self.primeiroFila.direita

            if self.primeiroFila is None:
                self.ultimoFila = None
            self._tamanho -= 1
            return elem
        raise IndexError("The queue is empty")

    # observar o primeiro da fila
    def peek(self):
        """Retorna o topo sem remover"""
        if self._tamanho > 0:
            elem = self.primeiroFila.dado
            return elem
        raise IndexError("The queue is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._tamanho


    def __repr__(self):
        if self._tamanho > 0:
            r = ""
            pointer = self.primeiroFila
            while(pointer):
                r = r + str(pointer.dado) + " "
                pointer = pointer.direita
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    fila = Queue()
    fila.push(1)
    fila.push(2)
    fila.push(3)
    fila.push(4)
    print(fila)
    print(fila.peek())
    fila.pop()
    print(fila)