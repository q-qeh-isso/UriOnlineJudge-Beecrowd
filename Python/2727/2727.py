while True:
    try:
        n = int(input())
        for p in range(n):
            cod = input().split()

            codGroups = len(cod) * 3 - 3
            char = ''
            if len(cod[0]) == 1:
                char = chr(97 + codGroups)
            elif len(cod[0]) == 2:
                char = chr(98 + codGroups)
            elif len(cod[0]) == 3:
                char = chr(99 + codGroups)

            print(char)

    except EOFError:
        break
