while True:
    try:
        N = int(input())  # atributos de cada carta
        M, L = input().split()  # numero de cartas Marcos e Leonardo
        M = int(M)
        L = int(L)

        baralho1 = []
        baralho2 = []

        for i in range(M + L):
            cartaAtributos = []
            cartaAtributos = input().split()
            if(i < M):
                baralho1.append(cartaAtributos)
            else:
                baralho2.append(cartaAtributos)

        C1, C2 = input().split()  # carta escolhida Marcos e Leonardo dentro de M e L
        C1 = int(C1)
        C2 = int(C2)
        A = int(input())

        if(int(baralho1[C1 - 1][A - 1]) > int(baralho2[C2 - 1][A - 1])):
            print('Marcos')
        elif(int(baralho1[C1 - 1][A - 1]) < int(baralho2[C2 - 1][A - 1])):
            print('Leonardo')
        else:
            print('Empate')

    except EOFError:
        break
