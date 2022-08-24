n = int(input())
for i in range(n):
    x = int(input())

    b = '{0:b}'.format(x)

    queimadas = b.split('0')
    maiorSeq = max(queimadas)

    print(len(maiorSeq))
