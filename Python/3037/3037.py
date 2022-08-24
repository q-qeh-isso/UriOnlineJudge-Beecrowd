N = int(input())

for i in range(N):
    maria = 0
    joao = 0
    vencedor = 'JOAO'
    for b in range(6):
        pontuacao, distancia = input().split()
        pontuacao = int(pontuacao)
        distancia = int(distancia)

        if(b < 3):
            joao += pontuacao * distancia
        else:
            maria += pontuacao * distancia

    if(joao < maria):
        vencedor = 'MARIA'
    else:
        vencedor = 'JOAO'

    print(vencedor)
