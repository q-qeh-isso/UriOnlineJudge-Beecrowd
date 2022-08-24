while True:
    try:
        n = int(input())

        qtd = 0
        while n != 1:
            n //= 2
            qtd += 1

        print(qtd)
    except EOFError:
        break
