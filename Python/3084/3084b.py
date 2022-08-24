while True:
    try:
        grHora, grMin = map(int, input().split())
    except EOFError:
        break

    hr = grHora // 30
    mi = grMin // 6

    print(f'{hr:02}:{mi:02}')
