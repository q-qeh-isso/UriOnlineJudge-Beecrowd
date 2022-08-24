linha1 = [float(x) for x in input().split()]
linha2 = [float(x) for x in input().split()]

total = 0

qtd = linha1[1]
preco = linha1[2]
total += qtd * preco
qtd = linha2[1]
preco = linha2[2]
total += qtd * preco

print(f'VALOR A PAGAR: R$ {total:.2f}')
