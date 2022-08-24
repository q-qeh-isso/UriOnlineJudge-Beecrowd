n = int(input())
for u in range(n):
    fibo = int(input())
    lista = list()
    for i in range(fibo + 1):
        if i == 0:
            lista.append(0)
        elif i <= 2:
            lista.append(1)
        else:
            lista.append(lista[i - 1] + lista[i - 2])

    print(f'Fib({fibo}) = {lista[-1]}')
