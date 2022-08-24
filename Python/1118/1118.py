novoCalculo = 1
while novoCalculo == 1:

    notasValidas = 0
    media = 0
    while notasValidas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notasValidas += 1
            media += nota
        else:
            print('nota invalida')

    print(f'media = {media / notasValidas:.2f}')
    while True:
        print('novo calculo (1-sim 2-nao)')
        nC = int(input())
        if nC == 1 or nC == 2:
            novoCalculo = nC
            break
