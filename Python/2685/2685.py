# teste = []
while True:
    try:
        m = int(input())
        # if m == -1: break
        m = m / 360

        # print(m)
        if m < 0.25 or m == 1:
            print('Bom Dia!!')
            # teste.append('Bom Dia!!')
        elif m >= 0.25 and m < 0.50:
            print('Boa Tarde!!')
            # teste.append('Boa Tarde!!')
        elif m >= 0.50 and m < 0.75:
            print('Boa Noite!!')
            # teste.append('Boa Noite!!')
        elif m >= 0.75 and m < 1:
            print('De Madrugada!!')
            # teste.append('De Madrugada!!')

    except EOFError:
        break

# print(*teste, sep='\n')
