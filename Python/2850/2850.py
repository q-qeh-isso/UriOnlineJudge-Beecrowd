while True:
    try:
        n = input()
    except EOFError:
        break

    if n == 'nenhuma':
        print('portugues')
    elif n == 'as duas':
        print('caiu')
    elif n == 'esquerda':
        print('ingles')
    elif n == 'direita':
        print('frances')
