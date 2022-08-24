num = float(input())
reajuste = 0
percentual = 0
if 0 <= num <= 400:
    reajuste = num * 0.15
    percentual = 15
elif 400 < num <= 800:
    reajuste = num * 0.12
    percentual = 12
elif 800 < num <= 1200:
    reajuste = num * 0.1
    percentual = 10
elif 1200 < num <= 2000:
    reajuste = num * 0.07
    percentual = 7
else:
    reajuste = num * 0.04
    percentual = 4

print(f'Novo salario: {num+reajuste:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')
