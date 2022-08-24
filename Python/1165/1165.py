N = int(input())

for i in range(0, N):
    numero = int(input())
    qtdResto0 = 0

    for b in range(1, numero + 1):
        if(numero % b == 0):
            qtdResto0 += 1

    if(qtdResto0 == 2):
        print(f'{numero} eh primo')
    else:
        print(f'{numero} nao eh primo')
