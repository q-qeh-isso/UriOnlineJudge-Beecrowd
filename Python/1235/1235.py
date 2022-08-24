while True:
    try:
        n = int(input())
    except EOFError:
        break

    for i in range(n):
        sent = input()
        left = sent[:len(sent) // 2]
        right = sent[-1:len(sent) // 2 - 1:-1]
        print(f'{left[::-1]}{right}')
