while True:
    try:
        n = int(input())
        for i in range(n):
            w = int(input())
            if w <= 8000:
                print('Inseto!')
            else:
                print('Mais de 8000!')
    except EOFError:
        break
