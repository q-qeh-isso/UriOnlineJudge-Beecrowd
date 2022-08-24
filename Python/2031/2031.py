n = int(input())

for k in range(n):
    res = 'Sem ganhador'
    jog1 = input()
    jog2 = input()

    if jog1 == 'ataque':
        if jog2 == 'pedra': res = 'Jogador 1 venceu'
        elif jog2 == 'papel': res = 'Jogador 1 venceu'
        elif jog2 == 'ataque': res = 'Aniquilacao mutua'
    elif jog1 == 'pedra':
        if jog2 == 'ataque': res = 'Jogador 2 venceu'
        elif jog2 == 'papel': res = 'Jogador 1 venceu'
        elif jog2 == 'pedra': res = 'Sem ganhador'
    elif jog1 == 'papel':
        if jog2 == 'pedra': res = 'Jogador 2 venceu'
        elif jog2 == 'ataque': res = 'Jogador 2 venceu'
        elif jog2 == 'papel': res = 'Ambos venceram'

    print(res)
