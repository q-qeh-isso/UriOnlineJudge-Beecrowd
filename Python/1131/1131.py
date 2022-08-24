novoGrenal = 1
interVitorias = 0
gremioVitorias = 0
empates = 0
qtdJogos = 0
while novoGrenal == 1:
    qtdJogos += 1
    interGols, gremioGols = [int(x) for x in input().split()]
    if interGols > gremioGols:
        interVitorias += 1
    elif interGols < gremioGols:
        gremioVitorias += 1
    else:
        empates += 1

    while True:
        print('Novo grenal (1-sim 2-nao)')
        nG = int(input())
        if nG == 1 or nG == 2:
            novoGrenal = nG
            break

print(f'{qtdJogos} grenais')
print(f'Inter:{interVitorias}')
print(f'Gremio:{gremioVitorias}')
print(f'Empates:{empates}')
if interVitorias > gremioVitorias:
    print('Inter venceu mais')
elif interVitorias < gremioVitorias:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
