positivos = 0
somaPositivos = 0
for i in range(6):
    num = float(input())
    if num == 0:
        continue
    if num > 0:
        positivos += 1
        somaPositivos += num
print(f'{positivos} valores positivos')
print(f'{somaPositivos/positivos:.1f}')
