n = int(input())
lst = [int(x) for x in input().split()]
menor = lst[0]
idx = 0
for i in range(1, len(lst)):
    if lst[i] < menor:
        menor = lst[i]
        idx = i

print(f'Menor valor: {menor}')
print(f'Posicao: {idx}')
