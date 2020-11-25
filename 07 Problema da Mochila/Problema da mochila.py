"""
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
30 = DINHEIRO QUE TENHO
7 = JOGADORES

NOME | CUSTO | PONTOS:

messi;20;370                74%
cristiano ronaldo;16;210    33.6%
-> neymar;14;290            40.6%
suarez;10;170               17%
-> cavani;7;150             10.5%
mbappe;11;120               13.2%
-> di maria;9;180           16.2%

———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Print de saída:

620
30
neymar
cavani
di maria
———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""

def mochilaInteira_BottomUp(W, valores, pontos, n, matriz):
    i = 0
    while i <= n:
        w = 0
        while w <= W:
            if i == 0 or w == 0:
                matriz[i][w] = 0
            elif pontos[i-1] <= w:
                matriz[i][w] = max(valores[i-1] + matriz[i-1][w-pontos[i-1]], matriz[i-1][w])
            else:
                matriz[i][w] = matriz[i-1][w]
            w+=1
        i+=1
    
    # PEGANDO AS POSIÇÕES QUE FORAM ACESSADAS.
    index = n 
    index2 = W 
    wilson = 0
    indexAcessados = []
    pesosAcessados = []
    while matriz[index][index2] > 0:
        if matriz[index-1][index2] != matriz[index][index2]:
            indexAcessados.append(valores.index(valores[index-1])+1)
            pesosAcessados.append(pontos[valores.index(valores[index-1])])
            index2 = index2-pontos[index-1]
        index -= 1
    print(pontos)
    print(valores)
    indexAcessados.sort()
    pesosAcessados.sort()
    return indexAcessados, pesosAcessados, matriz[n][W]

def main():
    W = int(input())
    n = int(input())
    v = []
    w = []
    jogadores = []
    for x in range(int(n)):
        jogador = input().split(';')
        jogadores.append([jogador[0], jogador[1], jogador[2]])
        w.append(int(jogador[1]))
        v.append(int(jogador[2]))
    print(jogadores)
    # ————————————————————————————————— CRIANDO MATRIZ —————————————————————————————————
    matriz = []
    for x in range(n+1):
        matriz.append([0]*(W+1))
    # ————————————————————————————————— PRINT —————————————————————————————————
    indexAcessados, pesos, resposta = mochilaInteira_BottomUp(W, v, w, n, matriz)
    print(resposta)
    print(sum(pesos))
    for x in indexAcessados:
        index = x-1
        print(jogadores[index][0])

if __name__ == '__main__':
    main()

"""
Exemplos de Inputs:

30
7
messi;20;370
cristiano ronaldo;16;210
neymar;14;290
suarez;10;170
cavani;7;150
mbappe;11;120
di maria;9;180

20
10
Adriano;8;57
Robinho;3;28
Kaka;6;41
Ze Roberto;4;32
Rivaldo;2;15
Ronaldinho Gaucho;11;77
Romario;9;59
Roberto Carlos;8;64
Ronaldo;10;65
Pele;11;76

"""