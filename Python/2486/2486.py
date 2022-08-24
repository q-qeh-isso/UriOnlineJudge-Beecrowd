tabela = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}
while True:
    t = int(input())
    if t == 0:
        break

    s = 0
    for i in range(t):
        qtd, food = input().split(' ', 1)
        qtd = int(qtd)

        for k in tabela:
            if k == food:
                s += tabela[k] * qtd
                break

    if s > 130:
        print(f'Menos {s-130} mg')
    elif s < 110:
        print(f'Mais {110-s} mg')
    else:
        print(f'{s} mg')
