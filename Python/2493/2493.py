while True:
    try:
        t = int(input())
        players = []
        respostas = []
        for i in range(t):
            conta, res = input().split('=')
            c1, c2 = conta.split()
            res = int(res)
            c1 = int(c1)
            c2 = int(c2)
            if c1 + c2 == res:
                respostas.append('+')
            elif c1 - c2 == res:
                respostas.append('-')
            elif c1 * c2 == res:
                respostas.append('*')
            else:
                respostas.append('I')

        for i in range(t):
            players.append(input())

        perdedores = []
        for i in range(len(players)):
            nome, escolha, op = players[i].split()
            escolha = int(escolha)
            if op != respostas[escolha - 1]:
                perdedores.append(nome)

        if len(perdedores) == len(players):
            print('None Shall Pass!')
        elif len(perdedores) == 0:
            print('You Shall All Pass!')
        else:
            perdedores.sort()
            for k in range(len(perdedores)):
                if k == len(perdedores) - 1:
                    print(f'{perdedores[k]}')
                else:
                    print(f'{perdedores[k]} ', end='')

    except EOFError:
        break
