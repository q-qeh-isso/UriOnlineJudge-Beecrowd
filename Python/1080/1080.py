maiorNumero = 0
posicaoNumero = 1
count = 1
while (count <= 100):  # alterar valor 100 para testar
    num = int(input())

    if(num >= maiorNumero):
        maiorNumero = num
        posicaoNumero = count

    count += 1

print(f'{maiorNumero}\n{posicaoNumero}')
