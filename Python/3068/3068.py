caso = 1
while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0:
        break
    meteors = int(input())

    qtd = 0
    for i in range(meteors):
        mX, mY = map(int, input().split())
        if (mX >= x1 and mY <= y1) and (mX <= x2 and mY >= y2):
            qtd += 1

    print('Teste', caso)
    print(qtd)
    caso += 1
