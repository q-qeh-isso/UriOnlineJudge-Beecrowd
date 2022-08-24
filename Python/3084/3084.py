while True:
    try:
        grHora, grMin = map(int, input().split())
    except EOFError:
        break

    hr = 0
    mi = 0
    if grHora != 0 and grMin != 0:
        hr = grHora // 30
        mi = grMin // 6
    elif grHora == 0 and grMin != 0:
        hr = 0
        mi = grMin // 6
    elif grHora != 0 and grMin == 0:
        hr = grHora // 30
        mi = 0

    print(f'{hr:02}:{mi:02}')
