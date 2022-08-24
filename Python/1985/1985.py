qtd = int(input())
total = 0
for i in range(qtd):
    p, q = [int(x) for x in input().split()]
    if p == 1001:
        total += q * 1.50
    elif p == 1002:
        total += q * 2.50
    elif p == 1003:
        total += q * 3.50
    elif p == 1004:
        total += q * 4.50
    elif p == 1005:
        total += q * 5.50

print(f'{total:.2f}')
