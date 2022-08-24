N = int(input())

for i in range(0, N):
    numero = int(input())
    somaDivisores = 0

    for b in range(1, numero):
        if(numero % b == 0):
            somaDivisores += b

    if(somaDivisores == numero):
        print(f'{numero} eh perfeito')
    else:
        print(f'{numero} nao eh perfeito')
