while True:
    try:
        dici = input()
        lampadas = int(input())
        piscadas = [int(x) for x in input().split()]

        msg = ''
        for i in piscadas:
            msg += dici[i - 1]

        print(msg)
    except EOFError:
        break
