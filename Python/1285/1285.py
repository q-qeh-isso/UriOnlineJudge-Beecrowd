while True:
    try:
        N, M = input().split()
        qtd = 0
        for i in range(int(N), int(M) + 1):
            charsList = list(str(i))
            charsSet = set(str(i))
            if(len(charsList) == len(charsSet)):
                qtd += 1

        print(qtd)
    except EOFError:
        break
