n = int(input())
jogo = [[0] * 3 for _ in range(2)]
for i in range(n):
    atletaNome = input()
    grauDif = float(input())
    pontos = sorted([float(x) for x in input().split()])
    pontos = sum(pontos[1:-1])
    print(f'{atletaNome} {pontos * grauDif:.2f}')
