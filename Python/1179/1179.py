lstPares = []
lstImpares = []


def showLista(tipo, lst):
    for i in range(len(lst)):
        print(f'{tipo}[{i}] = {lst[i]}')


for i in range(15):
    n = int(input())
    if n % 2 == 0:
        if len(lstPares) < 5:
            lstPares.append(n)
            if len(lstPares) == 5:
                showLista('par', lstPares)
                lstPares = []
    else:
        if len(lstImpares) < 5:
            lstImpares.append(n)
            if len(lstImpares) == 5:
                showLista('impar', lstImpares)
                lstImpares = []

showLista('impar', lstImpares)
showLista('par', lstPares)
