n = int(input())
carrinhos = 0
bonecas = 0
for i in range(n):
    n, s = input().split()
    if s == 'F':
        bonecas += 1
    else:
        carrinhos += 1

print(f'{carrinhos} carrinhos')
print(f'{bonecas} bonecas')
