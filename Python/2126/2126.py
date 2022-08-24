caso = 1
while True:
    try:
        n1 = input()
        n2 = input()
        qtd = 0
        pos = 0
        for i in range(len(n2)):
            if n2[i:].startswith(n1):
                qtd += 1
                pos = i

        print(f'Caso #{caso}:')
        if qtd == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {qtd}')
            print(f'Pos: {pos + 1}')
        print()

        caso += 1

    except EOFError:
        break
