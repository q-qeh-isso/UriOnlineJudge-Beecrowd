hrInicial, hrFinal = input().split()
hrInicial = int(hrInicial)
hrFinal = int(hrFinal)
duracao = 0

if(hrInicial == hrFinal):
    duracao = 24
else:
    if(hrFinal > hrInicial):
        duracao = hrFinal - hrInicial
    else:
        duracao = (24 - hrInicial) + hrFinal

print(f'O JOGO DUROU {duracao} HORA(S)')
