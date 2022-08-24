n = int(input())
jogo = [[0] * 3 for _ in range(2)]
for i in range(n):
    input()
    tentaGame = [int(x) for x in input().split()]
    sucessGame = [int(x) for x in input().split()]
    jogo[0][0] += tentaGame[0]
    jogo[0][1] += tentaGame[1]
    jogo[0][2] += tentaGame[2]
    jogo[1][0] += sucessGame[0]
    jogo[1][1] += sucessGame[1]
    jogo[1][2] += sucessGame[2]

ptsSaque = (jogo[1][0] / jogo[0][0]) * 100
ptsBlock = (jogo[1][1] / jogo[0][1]) * 100
ptsAtk = (jogo[1][2] / jogo[0][2]) * 100
print(f'Pontos de Saque: {ptsSaque:.2f} %.')
print(f'Pontos de Bloqueio: {ptsBlock:.2f} %.')
print(f'Pontos de Ataque: {ptsAtk:.2f} %.')
