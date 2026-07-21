# Note to self: o Computador joga aleátoriamente, posteriormente, adicionar lógica
posicoes_vazias = []
import random
tabuleiro = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for linha in tabuleiro:
    print(linha)
ganhou = False

while True:
    posicoes_vazias = []
    posicao = int(input("Digite onde quer colocar:"))
    linha1 =(posicao -1) //3
    coluna1 =(posicao -1) %3
    if tabuleiro[linha1][coluna1] == "X" or tabuleiro[linha1][coluna1] == "O":
        print("Já existe uma peça nesse lugar")
        continue  # ← Volta pro início, jogador tenta novamente
    else:
        tabuleiro[linha1][coluna1] = "X"
        for linha in tabuleiro:
            print(linha)
        print("----------------")
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro [i][j] != "X" and tabuleiro [i][j] != "O":
                posicao = i * 3 + j + 1
                posicoes_vazias.append(posicao)
    for linha in tabuleiro:
        if linha.count("X") == 3:
            print("You Win!")
            ganhou = True
            break
        if linha.count("O") == 3:
            print("You Lose!")
            ganhou = True
            break
    for j in range(len(tabuleiro)):
        coluna = []
        for i in range(len(tabuleiro)):
            coluna.append(tabuleiro[i][j])
        if coluna.count("X") == 3:
            print("You Win!")
            ganhou = True
        if coluna.count("O") == 3:
            print("You Lose!")
            ganhou = True
    diagonal = []
    for i in range(len(tabuleiro)):
        diagonal.append(tabuleiro[i][i])
    if diagonal.count("X") == 3:
        print("You Win!")
        ganhou = True
    if diagonal.count("O") == 3:
        print("You Lose!")
        ganhou = True
    diagonal = []
    for i in range(len(tabuleiro)):
        j = 2 - i
        diagonal.append(tabuleiro[i][j])
    if diagonal.count("X") == 3:
        print("You Win!")
        ganhou = True
    if diagonal.count("O") == 3:
        print("You Lose!")
        ganhou = True
    if len(posicoes_vazias) == 0:
        print("Draw")
        ganhou = True
    else:
        posicaopc = random.choice(posicoes_vazias)
        linhapc = (posicaopc - 1) // 3
        colunapc = (posicaopc - 1) % 3
        tabuleiro[linhapc][colunapc] = "O"
    for linha_display in tabuleiro:
        print(linha_display)

    if ganhou:
        break